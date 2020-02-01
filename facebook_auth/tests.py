from django.shortcuts import render
from bson.json_util import dumps
from django.http import HttpResponse,JsonResponse
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign as AdCampaign
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser
from facebook_business.adobjects.adset import AdSet
from allauth.socialaccount.models import (
    SocialAccount,
    SocialApp,
    SocialToken
    )


import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


my_app_id = SocialApp.client_id
my_app_secret = '0e51c739872e518f388fbf1439b6d7e7'
my_access_token = 'EAAt6AfVaOUABAJZBOoHMic2IZAADP3QpJyRwev57FUJIvkSUtAo5ZATcmYLb7EgqOLZB0RAhHKYupyxnbmRlDzjRJDtSKKjCnR6KaVw0n3HnHM6FsKf4We9ynZBVjrBs9GfDdSm4y94bZCcJjLHv56npCfrHWn3WBRePPs6mD4WwZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
me = AdUser(fbid='me')
my_account = me.get_ad_account()
for campaign in my_account.get_ad_campaigns(fields=[AdCampaign.Field.name]):
    for stat in campaign.get_stats(fields=[
        'impressions',
        'clicks',
        'spent',
        'unique_clicks',
        'actions',
    ]):
        print(campaign[campaign.Field.name])