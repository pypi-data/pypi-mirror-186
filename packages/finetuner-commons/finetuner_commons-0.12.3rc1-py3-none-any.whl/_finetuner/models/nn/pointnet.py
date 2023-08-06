# inspired by
#   https://github.com/DylanWusee/pointconv_pytorch/blob/master/utils/pointconv_util.py
#   https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet2_utils.py
#   https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet2_cls_msg.py

import torch
import torch.nn as nn
import torch.nn.functional as F


def square_distance(src, dst):
    """
    Calculate Euclid distance between each two points.
    src^T * dst = xn * xm + yn * ym + zn * zm;
    sum(src^2, dim=-1) = xn*xn + yn*yn + zn*zn;
    sum(dst^2, dim=-1) = xm*xm + ym*ym + zm*zm;
    dist = (xn - xm)^2 + (yn - ym)^2 + (zn - zm)^2
         = sum(src**2,dim=-1)+sum(dst**2,dim=-1)-2*src^T*dst
    Input:
        src: source points, [B, N, C]
        dst: target points, [B, M, C]
    Output:
        dist: per-point square distance, [B, N, M]
    """
    B, N, _ = src.shape
    _, M, _ = dst.shape
    dist = -2 * torch.matmul(src, dst.permute(0, 2, 1))
    dist += torch.sum(src**2, -1).view(B, N, 1)
    dist += torch.sum(dst**2, -1).view(B, 1, M)
    return dist


def index_points(points, idx):
    """
    Input:
        points: input points data, [B, N, C]
        idx: sample index data, [B, S]
    Return:
        new_points: coordinates of the centroids, indexed points data, [B, S, C]
    """
    device = points.device
    B = points.shape[0]
    view_shape = list(idx.shape)
    view_shape[1:] = [1] * (len(view_shape) - 1)
    repeat_shape = list(idx.shape)
    repeat_shape[0] = 1
    batch_indices = (
        torch.arange(B, dtype=torch.long)
        .to(device)
        .view(view_shape)
        .repeat(repeat_shape)
    )
    new_points = points[batch_indices, idx, :]
    return new_points


def farthest_point_sample(xyz, npoint):
    """
    Input:
        xyz: pointcloud data, which is xyz coordinates and corresponding
            features (if exist), [B, N, C] (B: batch size, N: number of points C: number of channels)
        npoint: number of selected samples
    Return:
        centroids: sampled pointcloud index, [B, npoint]
    """
    # import ipdb; ipdb.set_trace()
    device = xyz.device
    B, N, C = xyz.shape
    # centroids : the indices of sampled points of each sample in batch
    centroids = torch.zeros(B, npoint, dtype=torch.long).to(device)
    # distance : the minimum distance of point clouds to the last selected point, 1e10 : infinity value
    distance = torch.ones(B, N).to(device) * 1e10
    # farthest = torch.randint(0, N, (B,), dtype=torch.long).to(device)
    # farthest : indices of farthest points of each batch sample
    farthest = torch.zeros(B, dtype=torch.long).to(device)
    # batch_indices : batch indices of batch samples, [0, 1, 2, ..., B - 1]
    batch_indices = torch.arange(B, dtype=torch.long).to(device)
    # n iterations
    for i in range(npoint):
        centroids[:, i] = farthest
        centroid = xyz[batch_indices, farthest, :].view(B, 1, 3)
        # xyz - centroid is the difference of points and last selected centroid
        dist = torch.sum((xyz - centroid) ** 2, -1)
        mask = dist < distance
        # update corresponding distance item if dist < distance
        distance[mask] = dist[mask]
        # indices of farthest ones to the last selected centroids of each batch sample
        farthest = torch.max(distance, -1)[1]
    return centroids


def query_ball_point(radius, nsample, xyz, new_xyz):
    """
    Input:
        radius: local region radius
        nsample: max sample number in local region
        xyz: all points, [B, N, C]
        new_xyz: query points, [B, S, C]
    Return:
        group_idx: grouped points index, [B, S, nsample]
    """
    device = xyz.device
    B, N, C = xyz.shape
    _, S, _ = new_xyz.shape
    group_idx = (
        torch.arange(N, dtype=torch.long).to(device).view(1, 1, N).repeat([B, S, 1])
    )
    sqrdists = square_distance(new_xyz, xyz)
    group_idx[sqrdists > radius**2] = N
    group_idx = group_idx.sort(dim=-1)[0][:, :, :nsample]
    group_first = group_idx[:, :, 0].view(B, S, 1).repeat([1, 1, nsample])
    mask = group_idx == N
    group_idx[mask] = group_first[mask]
    return group_idx


def knn_point(nsample, xyz, new_xyz):
    """
    Input:
        nsample: max sample number in local region
        xyz: all points, [B, N, C]
        new_xyz: query points, [B, S, C]
    Return:
        group_idx: grouped points index, [B, S, nsample]
    """
    sqrdists = square_distance(new_xyz, xyz)
    _, group_idx = torch.topk(sqrdists, nsample, dim=-1, largest=False, sorted=False)
    return group_idx


def sample_and_group(npoint, nsample, xyz, points, density_scale=None):
    """
    Input:
        npoint:
        nsample:
        xyz: input points position data, [B, N, C]
        points: input points data, [B, N, D]
        density_scale:
    Return:
        new_xyz: sampled points position data, [B, 1, C]
        new_points: sampled points data, [B, 1, N, C+D]
    """
    B, N, C = xyz.shape
    S = npoint
    # fps_idx : indices of centroids
    fps_idx = farthest_point_sample(xyz, npoint)  # [B, npoint, C]
    # new_xyz : xyz of centroids
    new_xyz = index_points(xyz, fps_idx)
    # idx : indices of members in each knn group
    idx = knn_point(nsample, xyz, new_xyz)
    # grouped_xyz : xyz of members in each knn group
    grouped_xyz = index_points(xyz, idx)  # [B, npoint, nsample, C]
    # grouped_xyz_norm : the relative xyz to centroids in each knn group
    grouped_xyz_norm = grouped_xyz - new_xyz.view(B, S, 1, C)
    if points is not None:
        # grouped_points : features learned from previous layers
        grouped_points = index_points(points, idx)
        new_points = torch.cat(
            # relative xyz, features learned from previous layers
            [grouped_xyz_norm, grouped_points],
            dim=-1,
        )  # [B, npoint, nsample, C+D]
    else:
        new_points = grouped_xyz_norm

    if density_scale is None:
        return new_xyz, new_points, grouped_xyz_norm, idx
    else:
        grouped_density = index_points(density_scale, idx)
        return new_xyz, new_points, grouped_xyz_norm, idx, grouped_density


def sample_and_group_all(xyz, points, density_scale=None):
    """
    Input:
        xyz: input points position data, [B, N, C]
        points: input points data, [B, N, D]
    Return:
        new_xyz: sampled points position data, [B, 1, C]
        new_points: sampled points data, [B, 1, N, C+D]
    """
    B, N, C = xyz.shape
    # new_xyz = torch.zeros(B, 1, C).to(device)
    new_xyz = xyz.mean(dim=1, keepdim=True)
    grouped_xyz = xyz.view(B, 1, N, C) - new_xyz.view(B, 1, 1, C)
    if points is not None:
        new_points = torch.cat([grouped_xyz, points.view(B, 1, N, -1)], dim=-1)
    else:
        new_points = grouped_xyz
    if density_scale is None:
        return new_xyz, new_points, grouped_xyz
    else:
        grouped_density = density_scale.view(B, 1, N, 1)
        return new_xyz, new_points, grouped_xyz, grouped_density


def group(nsample, xyz, points):
    """
    Input:
        npoint:
        nsample:
        xyz: input points position data, [B, N, C]
        points: input points data, [B, N, D]
    Return:
        new_xyz: sampled points position data, [B, 1, C]
        new_points: sampled points data, [B, 1, N, C+D]
    """
    B, N, C = xyz.shape
    S = N
    new_xyz = xyz
    idx = knn_point(nsample, xyz, new_xyz)
    grouped_xyz = index_points(xyz, idx)  # [B, npoint, nsample, C]
    grouped_xyz_norm = grouped_xyz - new_xyz.view(B, S, 1, C)
    if points is not None:
        grouped_points = index_points(points, idx)
        new_points = torch.cat(
            [grouped_xyz_norm, grouped_points], dim=-1
        )  # [B, npoint, nsample, C+D]
    else:
        new_points = grouped_xyz_norm

    return new_points, grouped_xyz_norm


class PointNetSetAbstraction(nn.Module):
    def __init__(self, npoint, nsample, radius, in_channel, mlp, group_all):
        """_summary_
        Args:
            npoint (_type_): _description_
            nsample (_type_): _description_
            radius (_type_): _description_
            in_channel (_type_): _description_
            mlp (_type_): _description_
            group_all (_type_): _description_
        """
        super(PointNetSetAbstraction, self).__init__()
        self.npoint = npoint
        self.nsample = nsample
        self.radius = radius
        self.mlp_convs = nn.ModuleList()
        self.mlp_bns = nn.ModuleList()
        last_channel = in_channel
        for out_channel in mlp:
            self.mlp_convs.append(nn.Conv2d(last_channel, out_channel, 1))
            self.mlp_bns.append(nn.BatchNorm2d(out_channel))
            last_channel = out_channel
        self.group_all = group_all

    def forward(self, xyz, points):
        xyz = xyz.permute(0, 2, 1)
        if points is not None:
            points = points.permute(0, 2, 1)
        if self.group_all:
            new_xyz, new_points, _ = sample_and_group_all(xyz, points)
        else:
            # sample layer and group layer
            new_xyz, new_points, _, _ = sample_and_group(
                self.npoint, self.nsample, xyz, points
            )

        # new_xyz : sampled points position data [B, npoint, C]
        # new_points: sampled points data [B, npoint, nsample, C + D]
        new_points = new_points.permute(0, 3, 2, 1)  # [B, C+D, nsample,npoint]

        # PointNet layer
        for i, conv in enumerate(self.mlp_convs):
            bn = self.mlp_bns[i]
            new_points = F.relu(bn(conv(new_points)))
        new_points = torch.max(new_points, 2)[0]
        new_xyz = new_xyz.permute(0, 2, 1)
        return new_xyz, new_points


class PointNetSetAbstractionMsg(nn.Module):
    def __init__(self, npoint, radius_list, nsample_list, in_channel, mlp_list):
        super(PointNetSetAbstractionMsg, self).__init__()
        self.npoint = npoint
        self.radius_list = radius_list
        self.nsample_list = nsample_list
        self.conv_blocks = nn.ModuleList()
        self.bn_blocks = nn.ModuleList()

        # assert len(mlp_list) == len(radius_list)
        for i in range(len(mlp_list)):
            convs = nn.ModuleList()
            bns = nn.ModuleList()
            last_channel = in_channel + 3
            for out_channel in mlp_list[i]:
                convs.append(nn.Conv2d(last_channel, out_channel, 1))
                bns.append(nn.BatchNorm2d(out_channel))
                last_channel = out_channel
            self.conv_blocks.append(convs)
            self.bn_blocks.append(bns)

    def forward(self, xyz, points):
        xyz = xyz.permute(0, 2, 1)

        if points is not None:
            points = points.permute(0, 2, 1)

        B, N, C = xyz.shape
        S = self.npoint

        new_xyz = index_points(xyz, farthest_point_sample(xyz, S))
        new_points_list = []

        for i, radius in enumerate(self.radius_list):
            K = self.nsample_list[i]
            group_idx = query_ball_point(radius, K, xyz, new_xyz)
            grouped_xyz = index_points(xyz, group_idx)
            grouped_xyz -= new_xyz.view(B, S, 1, C)
            if points is not None:
                grouped_points = index_points(points, group_idx)
                grouped_points = torch.cat([grouped_points, grouped_xyz], dim=-1)
            else:
                grouped_points = grouped_xyz

            grouped_points = grouped_points.permute(0, 3, 2, 1)
            for j in range(len(self.conv_blocks[i])):
                conv = self.conv_blocks[i][j]
                bn = self.bn_blocks[i][j]
                grouped_points = F.relu(bn(conv(grouped_points)))
            new_points = torch.max(grouped_points, 2)[0]
            new_points_list.append(new_points)

        new_xyz = new_xyz.permute(0, 2, 1)
        new_points_concat = torch.cat(new_points_list, dim=1)
        return new_xyz, new_points_concat


class PointNetMLP(nn.Module):
    def __init__(
        self, input_dim: int = 2048, hidden_size: int = 4096, output_dim: int = 256
    ):
        super().__init__()
        self.output_dim = output_dim
        self.input_dim = input_dim
        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_size, bias=False),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_size, output_dim, bias=True),
        )

    def forward(self, x):
        x = self.model(x)
        return x


class PointNet2(nn.Module):
    def __init__(
        self,
        emb_dims=1024,
        input_shape='bnc',
        normal_channel=True,
        density_adaptive_type='ssg',
    ):
        super(PointNet2, self).__init__()

        if input_shape not in ['bnc', 'bcn']:
            raise ValueError(
                "Allowed shapes are 'bcn' (batch * channels * num_in_points), 'bnc' "
            )

        self.emb_dims = emb_dims
        self.input_shape = input_shape
        self.normal_channel = normal_channel

        if density_adaptive_type == 'ssg':
            if normal_channel:
                in_channel = 6
            else:
                in_channel = 3
            self.sa1 = PointNetSetAbstraction(
                npoint=512,
                radius=0.2,
                nsample=32,
                in_channel=in_channel,
                mlp=[64, 64, 128],
                group_all=False,
            )
            self.sa2 = PointNetSetAbstraction(
                npoint=128,
                radius=0.4,
                nsample=64,
                in_channel=128 + 3,
                mlp=[128, 128, 256],
                group_all=False,
            )
            self.sa3 = PointNetSetAbstraction(
                npoint=None,
                radius=None,
                nsample=None,
                in_channel=256 + 3,
                mlp=[256, 512, self.emb_dims],
                group_all=True,
            )
        else:
            if normal_channel:
                in_channel = 3
            else:
                in_channel = 0
            self.sa1 = PointNetSetAbstractionMsg(
                npoint=512,
                radius_list=[0.1, 0.2, 0.4],
                nsample_list=[16, 32, 128],
                in_channel=in_channel,
                mlp_list=[[32, 32, 64], [64, 64, 128], [64, 96, 128]],
            )
            self.sa2 = PointNetSetAbstractionMsg(
                npoint=128,
                radius_list=[0.2, 0.4, 0.8],
                nsample_list=[32, 64, 128],
                in_channel=320,
                mlp_list=[[64, 64, 128], [128, 128, 256], [128, 128, 256]],
            )
            self.sa3 = PointNetSetAbstraction(
                npoint=None,
                radius=None,
                nsample=None,
                in_channel=640 + 3,
                mlp=[256, 512, self.emb_dims],
                group_all=True,
            )

        self.fc1 = nn.Linear(self.emb_dims, 512)
        self.bn1 = nn.BatchNorm1d(512)
        self.fc2 = nn.Linear(512, 256)
        self.bn2 = nn.BatchNorm1d(256)

    def forward(self, xyz):
        if self.input_shape == 'bnc':
            xyz = xyz.permute(0, 2, 1)
            batch_size = xyz.shape[0]
        if self.normal_channel:
            norm = xyz[:, 3:, :]
            xyz = xyz[:, :3, :]
        else:
            norm = None

        l1_xyz, l1_points = self.sa1(xyz, norm)
        l2_xyz, l2_points = self.sa2(l1_xyz, l1_points)
        l3_xyz, l3_points = self.sa3(l2_xyz, l2_points)
        x = l3_points.view(batch_size, self.emb_dims)

        return x
