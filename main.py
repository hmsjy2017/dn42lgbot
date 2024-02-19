from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from base64 import b64decode

from utils import *

import os
import re
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hi! Welcome to Libecho Network's looking glass bot!")


def ping(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /ping [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Pinging...')
    msg.edit_text('```\n' + subprocess.run(
        ['ping', context.args[0], '-c', '4', '-W', '5'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def ping4(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /ping4 [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Pinging...')
    msg.edit_text('```\n' + subprocess.run(
        ['ping', context.args[0], '-c', '4', '-W', '5', '-4'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def ping6(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /ping6 [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Pinging...')
    msg.edit_text('```\n' + subprocess.run(
        ['ping', context.args[0], '-c', '4', '-W', '5', '-6'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def trace(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /traceroute [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Tracing route in 10s...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'traceroute', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def trace4(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /traceroute4 [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Tracing route in 10s...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'traceroute', '-4', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def trace6(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /traceroute6 [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Tracing route in 10s...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'traceroute', '-6', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def dig(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /dig [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Digging...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'dig', '+nocmd', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')

def dig6(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /dig6 [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Digging...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'dig', 'aaaa', '+nocmd', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')

def digall(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /digall [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Digging...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'dig', 'any', '+nocmd', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def nslookup(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /nslookup [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Querying...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'nslookup', context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


def whois(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text('Usage: /whois [target]')
        return
    if CERNET:
        if re.match(dn42_ipv4_pattern, context.args[0]) is None and re.match(neo_ipv4_pattern,
                                                                             context.args[0]) is None and not \
        context.args[0].endswith('.dn42') and not context.args[0].endswith('.neo'):
            update.message.reply_text('Only DN42 ping is allowed on Chinese nodes.')
            return
    msg = update.message.reply_text('Looking up whois...')
    msg.edit_text('```\n' + subprocess.run(
        ['timeout', '15s', 'whois', '-h', WHOIS_SERVER, context.args[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT).stdout.decode() + '\n```', parse_mode='MarkdownV2')


if __name__ == '__main__':
    dispatcher.add_handler(CommandHandler('start', start, run_async=True))
    dispatcher.add_handler(CommandHandler('ping', ping, run_async=True))
    dispatcher.add_handler(CommandHandler('ping4', ping4, run_async=True))
    dispatcher.add_handler(CommandHandler('ping6', ping6, run_async=True))
    dispatcher.add_handler(CommandHandler('trace', trace, run_async=True))
    dispatcher.add_handler(CommandHandler('trace4', trace4, run_async=True))
    dispatcher.add_handler(CommandHandler('trace6', trace6, run_async=True))
    dispatcher.add_handler(CommandHandler('dig', dig, run_async=True))
    dispatcher.add_handler(CommandHandler('dig6', dig6, run_async=True))
    dispatcher.add_handler(CommandHandler('digall', digall, run_async=True))
    dispatcher.add_handler(CommandHandler('nslookup', nslookup, run_async=True))
    dispatcher.add_handler(CommandHandler('whois', whois, run_async=True))

    updater.start_polling()

    updater.idle()
