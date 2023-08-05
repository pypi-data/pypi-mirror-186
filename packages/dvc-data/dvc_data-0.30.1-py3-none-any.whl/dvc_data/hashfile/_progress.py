from dvc_objects._tqdm import Tqdm


class QueryingProgress(Tqdm):
    def __init__(self, iterable=None, total=None, name=None, phase="Querying"):
        msg_part = "cache in " + f"'{name}'" if name else "remote cache"
        msg_fmt = "{phase} " + msg_part

        self._estimating_msg = msg_fmt.format(phase="Estimating size of")
        self._listing_msg = msg_fmt.format(phase="Querying")
        self.desc = desc = msg_fmt.format(phase=phase)
        super().__init__(
            iterable=iterable,
            desc=desc,
            total=total,
            unit="files",
            unit_scale=False,
            bar_format=self.BAR_FMT_DEFAULT,
        )

    def callback(self, phase, *args):
        total = args[0] if args else self.total
        completed = args[1] if len(args) > 1 else self.n
        if phase == "estimating":
            self.desc = self._estimating_msg
        elif phase == "querying":
            self.desc = self._listing_msg
        self.update_to(completed, total)
