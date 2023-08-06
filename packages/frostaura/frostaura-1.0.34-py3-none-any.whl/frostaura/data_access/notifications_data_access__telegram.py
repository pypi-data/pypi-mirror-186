'''This module defines the interface for the notifications data access components.'''
from telegram import ParseMode
from telegram.ext import Updater
import io
import matplotlib.pyplot as plt
import prettytable as pt
import pandas as pd
from frostaura.data_access.notifications_data_access import INotificationsDataAccess

class TelegramNotificationsDataAccess(INotificationsDataAccess):
    '''Component to perform resource related actions.'''

    def __init__(self, bot_token: str, chat_id: str, register_handlers = None):
        assert bot_token is not None

        self.bot_token = bot_token
        self.register_handlers = register_handlers

        self.updater = Updater(token=self.bot_token)
        self.dispatcher = self.updater.dispatcher
        self.bot = self.updater.bot
        self.chat_id = chat_id

        if self.register_handlers is not None:
            self.register_handlers(self.dispatcher)

        self.updater.start_polling()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, t_b):
        self.updater.stop()
        self.updater = None
        self.dispatcher = None
        self.bot = None

    def __get_figure_buffer__(self, figure: plt.Figure) -> io.BytesIO:
        buffer = io.BytesIO()
        figure.savefig(buffer, format='png')
        buffer.seek(0)

        return buffer

    def send_text(self, text: str):
        '''Send a text notification.'''

        self.bot.send_message(chat_id=self.chat_id, text=text, parse_mode=ParseMode.HTML)

    def send_figure(self, figure: plt.Figure):
        self.bot.send_photo(chat_id=self.chat_id, photo=self.__get_figure_buffer__(figure))

    def send_dataframe(self, dataframe: pd.DataFrame):
        table = pt.PrettyTable(tuple(dataframe.columns))
        
        for index, row in dataframe.iterrows():
            row_data = list()

            for column_name in dataframe.columns:
                row_data.append(row[column_name])
            
            table.add_row(row_data)

        self.bot.send_message(chat_id=self.chat_id, text=f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
