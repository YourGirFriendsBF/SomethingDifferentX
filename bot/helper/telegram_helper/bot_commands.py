from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = f'mirror11'
        self.UnzipMirrorCommand = f'unzipmirror11'
        self.ZipMirrorCommand = f'zipmirror11'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo'
        self.RmSudoCommand = f'rmsudo'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'clone11'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'watch11'
        self.ZipWatchCommand = f'zipwatch11'
        self.QbMirrorCommand = f'qbmirror11'
        self.QbUnzipMirrorCommand = f'qbunzipmirror11'
        self.QbZipMirrorCommand = f'qbzipmirror11'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leech{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'

BotCommands = _BotCommands()
