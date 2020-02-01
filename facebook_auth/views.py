from django.shortcuts import render
from bson.json_util import dumps
from django.http import HttpResponse,JsonResponse
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.page import Page
from facebook_business.adobjects.campaign import Campaign as AdCampaign
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser
from facebook_business.adobjects.adset import AdSet
from allauth.socialaccount.models import (
    SocialAccount,
    SocialApp,
    SocialToken
    ) 


def get_facebook_page(request):
    my_app_id = SocialApp.client_id
    my_app_secret = '0e51c739872e518f388fbf1439b6d7e7'
    my_access_token = 'EAAt6AfVaOUABAJZBOoHMic2IZAADP3QpJyRwev57FUJIvkSUtAo5ZATcmYLb7EgqOLZB0RAhHKYupyxnbmRlDzjRJDtSKKjCnR6KaVw0n3HnHM6FsKf4We9ynZBVjrBs9GfDdSm4y94bZCcJjLHv56npCfrHWn3WBRePPs6mD4WwZDZD'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    me = AdUser(fbid='me')
    my_pages = me.get_pages(fields=[Page.Field.name,Page.Field.id])
    my_ad_account = me.get_ad_accounts(fields=[AdAccount.Field.name,AdAccount.Field.id])
    namesAndAccIds = []
    namesAndAdaccIDs = []
    account_insieght = []
    page_likes = []
    for account in my_pages:
        namesAndAccIds.append((account['name'],account['id']))
    for adaccount in my_ad_account:
        namesAndAdaccIDs.append((adaccount['name'],adaccount['id']))
    return render(request,'index.html', locals())
    
def get_page_insight(request):
    my_app_id = SocialApp.client_id
    my_app_secret = '0e51c739872e518f388fbf1439b6d7e7'
    my_access_token = 'EAAt6AfVaOUABAJZBOoHMic2IZAADP3QpJyRwev57FUJIvkSUtAo5ZATcmYLb7EgqOLZB0RAhHKYupyxnbmRlDzjRJDtSKKjCnR6KaVw0n3HnHM6FsKf4We9ynZBVjrBs9GfDdSm4y94bZCcJjLHv56npCfrHWn3WBRePPs6mD4WwZDZD'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    me = AdUser(fbid='me')
    my_pages = me.get_pages(fields=[Page.Field.name,Page.Field.id])
    my_ad_account = me.get_ad_accounts(fields=[AdAccount.Field.name,AdAccount.Field.id])
    pass
