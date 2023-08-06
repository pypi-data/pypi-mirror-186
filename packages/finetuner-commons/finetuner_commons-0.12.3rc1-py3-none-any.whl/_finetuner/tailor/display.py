import abc

from rich import box, print
from rich.table import Table


class DisplayMixin(abc.ABC):
    @abc.abstractmethod
    def summary(self, *args, **kwargs):
        ...

    def display(self, *args, **kwargs) -> None:
        """
        Display the model architecture from :py:attr:`.summary` in a table.

        :param args: args pass to :py:attr:`.summary`
        :param kwargs: kwargs pass to :py:attr:`.summary`
        """
        _summary = self.summary(*args, **kwargs)
        table = Table(box=box.SIMPLE)
        cols = ['name', 'output_shape_display', 'nb_params', 'trainable']
        for k in cols:
            table.add_column(k)
        for s in _summary:
            if s['trainable']:
                style = 'bright_green'
            else:
                style = 'cyan'
            if 'identity' in s['name']:
                style = 'bright_black'  # overwrite style if it is an identity layer.
            table.add_row(*map(str, (s[v] for v in cols)), style=style)
        print(
            table,
            '[green]Green[/green] layers are trainable layers, '
            '[cyan]Cyan[/cyan] layers are non-trainable layers or frozen layers.\n'
            '[bright_black]Gray[/bright_black] layers indicates this layer has been '
            'replaced by an Identity layer.\n'
            'Use to_embedding_model(...) to create embedding model.',
        )
