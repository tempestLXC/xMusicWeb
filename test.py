import unittest
from NetEaseMusic import *


class Test_xMusicWeb(unittest.TestCase):
    def test_qq(self):
        l = qq.getList('https://y.qq.com/n/yqq/playlist/3363492195.html')
        res = [(u'\u8d81\u65e9', u'\u5f20\u60e0\u59b9', u'\u4e0d\u987e\u4e00\u5207'), (u'\u9ed1\u8272\u5e7d\u9ed8', u'\u5468\u6770\u4f26', u'Jay'), (u'\u4e3a\u4f60\u5199\u8bd7', u'\u5434\u514b\u7fa4', u'\u4e3a\u4f60\u5199\u8bd7'), (u'\u90a3\u4e2a\u7537\u4eba', u'\u6768\u5b97\u7eac', u'\u539f\u8272'), (u'Right Now (Na Na Na)', u'Akon', u'Promo Only Mainstream Radio November'), (u'\u4e0d\u80fd\u8bf4\u7684\u79d8\u5bc6', u'\u5468\u6770\u4f26', u'\u4e0d\u80fd\u8bf4\u7684\u79d8\u5bc6 \u7535\u5f71\u539f\u58f0\u5e26'), (u'Always Online', u'\u6797\u4fca\u6770', u'JJ\u9646'), (u'\u4e00\u4e2a\u4eba\u60f3\u7740\u4e00\u4e2a\u4eba', u'\u66fe\u6c9b\u6148', u'\u7ec8\u6781\u4e00\u73ed2 \u7535\u89c6\u5267\u539f\u58f0\u5e26'), (u'Halo', u'Beyonc\xe9', u'I Am... Sasha Fierce (Deluxe Version)'), (u'Hope', u'Tobu', u'Hope'), (u'\u660e\u5929\u8fc7\u540e', u'\u5f20\u6770', u'\u660e\u5929\u8fc7\u540e'), (u'Stay Here Forever', u'Jewel', u'Sweet and Wild (Deluxe Edition)'), (u'\u4eca\u5929\u4f60\u8981\u5ac1\u7ed9\u6211', u'\u8521\u4f9d\u6797/\u9676\u5586', u'J\u4e16\u7eaaJeneration\u5927\u724c'), (u'\u6696\u6696 (Live)', u'\u8303\u73ae\u742a', u'QQ\u97f3\u4e50\u5dc5\u5cf0\u5c0a\u4eab\u4f1a-\u8303\u73ae\u742a\u4e0a\u6d77\u5c0a\u4eab\u4f1a'), (u'\u6e29\u6696\u4f60\u7684\u51ac (\u5931\u604b\u7248)', u'\u6b27\u9633\u5a1c\u5a1c', u'\u6e29\u6696\u4f60\u7684\u51ac\uff08\u5931\u604b\u7248\uff09'), (u'\u623f\u95f4', u'\u5218\u745e\u7426', u'\u79c1\u623f\u6b4c'), (u'\u6f14\u5458', u'\u859b\u4e4b\u8c26', u'\u7ec5\u58eb'), (u'\u521a\u521a\u597d', u'\u859b\u4e4b\u8c26', u'\u521d\u5b66\u8005'), (u'\u4e00\u751f\u6709\u4f60', u'\u6c34\u6728\u5e74\u534e', u'\u4e00\u751f\u6709\u4f60'), (u'\u4f5c\u8005', u'\u9ad8\u8fdb', u'\u4f5c\u8005'), (u'\u4e00\u7b11\u503e\u57ce', u'\u6c6a\u82cf\u6cf7', u'\u5fae\u5fae\u4e00\u7b11\u5f88\u503e\u57ce \u7535\u89c6\u5267\u539f\u58f0\u5e26'), (u'\u7ed9\u6211\u4e00\u4e2a\u7406\u7531\u5fd8\u8bb0', u'A-Lin', u'\u5bc2\u5bde\u4e0d\u75db'), (u'\u542c\u6d77', u'\u5f20\u60e0\u59b9', u'\u60c5\u7275\u5973\u4eba\u5fc3'), (u'The Saltwater Room (Original Version)', u'Owl City/Breanne D\xfcren', u"Maybe I'm Dreaming"), (u'\u5750\u5728\u5df7\u53e3\u7684\u90a3\u5bf9\u7537\u5973', u'\u81ea\u7136\u5377', u"C'est La Vie"), (u'\u7ea2\u65e5 (\u7ca4\u8bed)', u'\u674e\u514b\u52e4', u'\u7ea2\u65e5'), (u'\u5f53\u4f60\u8001\u4e86', u'\u8d75\u7167', u'\u5f53\u4f60\u8001\u4e86'), (u'\u7261\u4e39\u6c5f', u'\u5357\u62f3\u5988\u5988', u'2\u53f7\u9910'), (u'\u91ce\u5b50 (Live)', u'\u82cf\u8fd0\u83b9', u'\u7b2c\u4e8c\u5b63\u4e2d\u56fd\u597d\u6b4c\u66f2\u5341\u5927\u91d1\u66f2'), (u'\u5bf9\u4e0d\u8d77\u6211\u7231\u4f60 (\u4e2d\u6587\u7248)', u'\u8521\u6df3\u4f73', u'\u6df3\u5267\u4f73\u66f2 \u7535\u89c6\u5267\u539f\u58f0\u5e26'), (u'\u4e00\u4e07\u4e2a\u820d\u4e0d\u5f97', u'\u5e84\u5fc3\u598d', u'\u5e84\u5fc3\u598d\u60c5\u6b4c\u7cbe\u9009\u96c6'), (u'\u9690\u5f62\u7684\u7fc5\u8180', u'\u5f20\u97f6\u6db5', u'\u6f58\u6735\u62c9'), (u'\u66a7\u6627', u'\u6768\u4e1e\u7433', u'\u66a7\u6627'), (u'\u6325\u7740\u7fc5\u8180\u7684\u5973\u5b69', u'\u5bb9\u7956\u513f', u'\u72ec\u7167'), (u'\u6211\u7684\u6b4c\u58f0\u91cc', u'\u66f2\u5a49\u5a77', u'Everything In The World (\u767d\u91d1\u5e86\u529f\u7248)'), (u'\u9f99\u5377\u98ce', u'G.E.M. \u9093\u7d2b\u68cb', u'\u9f99\u5377\u98ce'), (u'\u6700\u521d\u7684\u68a6\u60f3', u'\u8303\u73ae\u742a', u'\u6700\u521d\u7684\u68a6\u60f3'), (u'What Do You Mean?', u'Justin Bieber', u'What Do You Mean?'), (u'\u4f60\u88ab\u5199\u5728\u6211\u7684\u6b4c\u91cc', u'\u82cf\u6253\u7eff/Ella', u'\u4f60\u5728\u70e6\u607c\u4ec0\u4e48'), (u'\u6325\u7740\u7fc5\u8180\u7684\u5973\u5b69', u'\u5bb9\u7956\u513f', u'\u6211\u7684\u9a84\u50b2'), (u'\u6709\u4f60\u7684\u5feb\u4e50', u'\u738b\u82e5\u7433', u'Start From Here'), (u'\u660e\u5929\uff0c\u4f60\u597d', u'\u725b\u5976\u5496\u5561', u'Lost & Found\u53bb\u5bfb\u627e'), (u'\u5341\u4e00\u5e74', u'\u90b1\u6c38\u4f20', u'\u5341\u4e00\u5e74'), (u'\u8d70\u7740\u8d70\u7740\u5c31\u6563\u4e86', u'\u5e84\u5fc3\u598d', u'\u8d70\u7740\u8d70\u7740\u5c31\u6563\u4e86'), (u'\u8ba4\u771f\u7684\u96ea', u'\u859b\u4e4b\u8c26', u'\u672a\u5b8c\u6210\u7684\u6b4c'), (u'\u6211\u7684\u5929\u7a7a', u'\u5357\u5f81\u5317\u6218NZBZ', u'\u9752\u6625\u6d3e \u7535\u5f71\u539f\u58f0\u5e26'), (u'IF YOU', u'BIGBANG (\ube45\ubc45)', u'MADE SERIES \u300aD\u300b'), (u'\u6211\u4eec\u4e0d\u8be5\u8fd9\u6837\u7684', u'\u5f20\u8d6b\u5ba3', u'\u5317\u4e0a\u5e7f\u4e0d\u76f8\u4fe1\u773c\u6cea \u7535\u89c6\u5267\u539f\u58f0\u5e26'), (u'\u591a\u5e78\u8fd0', u'\u97e9\u5b89\u65ed', u'\u591a\u5e78\u8fd0'), (u'\u6211\u4eec\u90fd\u4e00\u6837', u'\u5f20\u6770', u'\u660e\u5929\u8fc7\u540e'), (u'\u4e0d\u518d\u8054\u7cfb', u'\u7a0b\u54cd', u'\u4e0d\u518d\u8054\u7cfb'), (u'\u4e0d\u518d\u8054\u7cfb', u'\u590f\u5929Alex', u'\u5206\u624b\u4fe1'), (u'\u591a\u559c\u6b22\u4f60', u'\u5c0f\u8d31\uff08\u8c2d\u51b0\u5c27\uff09', u'\u591a\u559c\u6b22\u4f60'), (u'\u6ca1\u6709\u4ec0\u4e48\u4e0d\u540c', u'\u66f2\u5a49\u5a77', u'Everything In The World (\u767d\u91d1\u5e86\u529f\u7248)'), (u'\u5c0f\u624b\u62c9\u5927\u624b (Live)', u'\u90d1\u6e6b\u6cd3', u''), (u'\u5f53\u6211\u5531\u8d77\u8fd9\u9996\u6b4c', u'\u5c0f\u8d31\uff08\u8c2d\u51b0\u5c27\uff09/\u661f\u5f1f', u'\u6211\u662f\u5c0f\u8d31'), (u'\u81f3\u5c11\u8fd8\u6709\u4f60', u'\u6797\u5fc6\u83b2', u"\u6797\u5fc6\u83b2's"), (u'\u5c0f\u5e78\u8fd0 (Live)', u'\u56fd\u6c11\u7f8e\u5c11\u5973\u56e2\u5458', u'\u56fd\u6c11\u7f8e\u5c11\u5973 \u7b2c3\u671f'), (u'\u5982\u679c\u8fd9\u5c31\u662f\u7231\u60c5', u'\u5f20\u9753\u9896', u'\u6211\u76f8\u4fe1'), (u'\u4e0d\u8bf4\u518d\u89c1', u'\u8bb8\u98de', u'\u4e0d\u8bf4\u518d\u89c1'), (u'Scream & Shout (Radio Edit)', u'will.i.am/Britney Spears', u"Now That's What I Call 21st Century"), (u'Moon Girl', u'Inna', u'I Am The Club Rocker'), (u'Insomnia', u'Craig David', u'Insomnia'), (u"Here's To Never Growing Up (Explicit)", u'Avril Lavigne', u"Here's to Never Growing Up"), (u'Fade', u'Alan Walker', u'Fade'), (u'\u597d\u60f3\u4f60', u'\u6731\u4e3b\u7231', u'\u56db\u53f6\u8349Joyce Chu \u540c\u540dEP'), (u'\u6d77\u5357\u6700\u6d41\u884c\u5916\u8bed\u6162\u6447\u54dd\u54dd (DJ\u7248)', u'DJ', u'DJ\u821e\u66f2(\u534e\u8bed)\u7cfb\u52179'), (u'Booty Music (\u56fd\u8bed)', u'\u4f59\u5fae\u96ea', u'\u6211\u662f\u4f59\u5fae\u96ea'), (u'\u4eb2\u7231\u7684\u90a3\u4e0d\u662f\u7231\u60c5 (Live)', u'\u5f20\u97f6\u6db5', u'\u9690\u85cf\u7684\u6b4c\u624b \u7b2c6\u671f'), (u'\u7ed9\u6211\u4e00\u9996\u6b4c\u7684\u65f6\u95f4', u'\u5468\u6770\u4f26', u'\u9b54\u6770\u5ea7'), (u'\u6674\u5929', u'\u5468\u6770\u4f26', u'\u53f6\u60e0\u7f8e'), (u'\u5b89\u9759', u'\u5468\u6770\u4f26', u'\u8303\u7279\u897f'), (u'\u5929\u540e', u'\u9648\u52bf\u5b89', u'\u5929\u540e'), (u'\u6709\u70b9\u751c', u'\u6c6a\u82cf\u6cf7/By2', u''), (u'\u4e00\u89c1\u949f\u60c5', u'\u67f3\u5ca9/\u9ec4\u707f\u76db', u''), (u'\u9999\u6c34\u6709\u6bd2', u'\u80e1\u6768\u6797', u''), (u'\u70df\u706b', u'\u9648\u7fd4', u''), (u'\u7231\u60c5\u8f6c\u79fb', u'\u9648\u5955\u8fc5', u'The 1st Eleven Years \u7136\u540e\u5462\uff1f'), (u'Booty Music', u'Git Fresh', u'Booty Music'), (u'Bubbly', u'Colbie Caillat', u'2007\u5e74Billboard Hot100'), (u'\u4e0d\u8981\u8bf4\u8bdd', u'\u9648\u5955\u8fc5', u'\u4e0d\u60f3\u653e\u624b'), (u'Bye Bye Bye', u'Lovestoned', u'Rising Love'), (u'\u4e11\u516b\u602a', u'\u859b\u4e4b\u8c26', u'\u610f\u5916'), (u'\u7b2c\u4e03\u611f', u'\u5f20\u9753\u9896', u'\u7b2c\u4e03\u611f'), (u'\u7236\u4eb2', u'\u7b77\u5b50\u5144\u5f1f', u'\u7236\u4eb2'), (u'Glad You Came', u'The Wanted', u'Glad You Came'), (u'\u597d\u5fc3\u5206\u624b', u'\u5362\u5de7\u97f3/\u738b\u529b\u5b8f', u'\u7537\u5973\u60c5\u6b4c\u5bf9\u5531\u51a0\u519b\u5168\u8bb0\u5f55'), (u'Heroes (we could be)', u'Alesso/Tove Lo', u'Forever'), (u'\u9ec4\u660f', u'\u5468\u4f20\u96c4', u'\u7231\u60c5\u4fdd\u9c9c\u76d2'), (u'\u5047\u5982', u'\u4fe1\u4e50\u56e2', u'\u6311\u4fe1 (\u65b0\u6b4c+\u7cbe\u9009)'), (u'\u5047\u5982\u7231\u6709\u5929\u610f', u'\u674e\u5065', u'\u674e\u5065'), (u'\u84dd\u83b2\u82b1', u'\u8bb8\u5dcd', u'\u66fe\u7ecf\u7684\u4f60'), (u'\u95f9\u591f\u4e86\u6ca1\u6709', u'\u8d56\u4f1f\u950b', u'\u7537\u670b\u5973\u53cb'), (u'\u5343\u91cc\u4e4b\u5916', u'\u8d39\u7389\u6e05', u'\u534e\u7eb3\u65b0\u58f0 Vol.1'), (u'\u5947\u5999\u80fd\u529b\u6b4c', u'\u9648\u7c92', u'\u9648\u7c92\u7684\u5355\u66f2\u5217\u8868'), (u'\u5982\u679c\u6709\u6765\u751f', u'\u8c2d\u7ef4\u7ef4', u'\u8c2d\u67d0\u67d0'), (u'\u5165\u620f\u592a\u6df1 (Remix)', u'\u9a6c\u65ed\u4e1c', u'\u5165\u620f\u592a\u6df1'), (u'See You Again', u'Wiz Khalifa/Charlie Puth', u'Furious 7 (Original Motion Picture Soundtrack)'), (u'\u5341\u5e74', u'\u9648\u5955\u8fc5', u'\u9ed1\u767d\u7070'), (u'\u5929\u4f7f\u7684\u7fc5\u8180', u'\u5b89\u7425', u'\u5929\u4f7f\u7684\u7fc5\u8180'), (u'Try', u'Colbie Caillat', u'Gypsy Heart Side A'), (u'Valder Fields', u'Tamas Wells', u'A Plea en Vendredi'), (u'\u6211\u5f88\u5feb\u4e50', u'\u5218\u60dc\u541b', u'\u7231\u60c5\u82b1\u56ed'), (u'\u6211\u4eec\u7ed3\u5a5a\u5427', u'\u91d1\u838e/\u5218\u4f73', u'\u4ed6\u4e0d\u7231\u6211'), (u'\u6211\u4e5f\u53ef\u4ee5\u662f\u6d41\u6d6a\u8bd7\u4eba', u'\u597d\u59b9\u59b9\u4e50\u961f', u'\u963f\u5f25\u9640\u4f5b\u4e48\u4e48\u54d2\xb7\u4e00\u4e2a\u5b69\u5b50\u7684\u5fc3\u613f'), (u'\u6211\u77e5\u9053', u'BY2', u'Twins'), (u'\u4e0b\u8f88\u5b50\u5982\u679c\u6211\u8fd8\u8bb0\u5f97\u4f60', u'\u9a6c\u90c1', u'\u604b\u4eba\u7d6e\u8bed'), (u'\u5c0f\u9152\u7a9d (\u56fd\u8bed)', u'\u8521\u5353\u598d/\u6797\u4fca\u6770', u'\u4e8c\u7f3a\u4e00'), (u'\u559c\u6b22\u4f60', u'G.E.M. \u9093\u7d2b\u68cb', u'\u559c\u6b22\u4f60'), (u'\u5fc3\u5899', u'\u90ed\u9759', u'\u5728\u6811\u4e0a\u5531\u6b4c'), (u'\u4ee5\u540e\u7684\u4ee5\u540e', u'\u5e84\u5fc3\u598d', u'\u9519\u7231\u60c5\u6b4c'), (u'\u4e00\u4e07\u6b21\u60b2\u4f24', u'\u9003\u8dd1\u8ba1\u5212', u'\u4e16\u754c'), (u'\u539f\u8c05', u'\u5f20\u7389\u534e', u'\u5f20\u7389\u534e'), (u'\u54b1\u4eec\u7ed3\u5a5a\u5427', u'\u9f50\u6668', u'\u54b1\u4eec\u7ed3\u5a5a\u5427'), (u'\u8d70\u5728\u51b7\u98ce\u4e2d', u'\u5218\u601d\u6db5', u'\u62e5\u62b1\u4f60'), (u'\u6211\u60f3\u6211\u4e0d\u591f\u597d', u'SOCO\u771f', u''), (u'\u5c4b\u9876', u'\u5468\u6770\u4f26/\u6e29\u5c9a', u''), (u'\u7231\u4f60\u6ca1\u9519', u'\u5f20\u4fe1\u54f2', u''), (u'\u9999\u6c34\u6709\u6bd2', u'\u6842\u83b9\u83b9', u'\u9999\u6c34\u6709\u6bd2'), (u'\u7a81\u7136\u7684\u81ea\u6211', u'\u4f0d\u4f70/China Blue', u'\u5fd8\u60c51015\u7cbe\u9009\u8f91'), (u'\u591c\u7a7a\u4e2d\u6700\u4eae\u7684\u661f', u'\u9003\u8dd1\u8ba1\u5212', u'\u4e16\u754c'), (u'\u65b0\u7684\u5fc3\u8df3', u'G.E.M. \u9093\u7d2b\u68cb', u'\u65b0\u7684\u5fc3\u8df3'), (u'\u5c0f\u60c5\u6b4c', u'\u82cf\u6253\u7eff', u'\u5c0f\u5b87\u5b99'), (u'\u4e61\u95f4\u7684\u5c0f\u8def\u4e0a', u'\u5218\u6e05\u6ca8', u'\u4e00\u7f15\u6e05\u6ca8'), (u'\u7ea2\u873b\u8713', u'\u5c0f\u864e\u961f', u'\u51ef\u65cb88-91\u8f89\u714c\u6218\u7ee9'), (u'\u6709\u70b9\u751c', u'\u6c6a\u82cf\u6cf7/BY2', u'\u4e07\u6709\u5f15\u529b'), (u'\u7a81\u7136\u597d\u60f3\u4f60', u'\u4e94\u6708\u5929', u'\u7231\u4f60\uff0c\u90a3\u4e9b\u5e74 \u56fd\u8bed\u60c5\u6b4c\u7cbe\u9009'), (u'\u7ec8\u70b9\u7ad9', u'\u8c22\u9706\u950b', u'\u7ed9\u81ea\u5df1\u7684\u60c5\u6b4c \u65b0\u66f2 + \u7cbe\u9009 2009'), (u'\u7a3b\u9999', u'\u5468\u6770\u4f26', u'\u9b54\u6770\u5ea7'), (u'\u6211\u4eec\u7684\u660e\u5929', u'\u9e7f\u6657', u'\u91cd\u8fd420\u5c81 \u7535\u5f71\u539f\u58f0\u5e26'), (u'Heroes (We Could Be)', u'Alesso/Tove Lo', u'Forever (Deluxe)'), (u'\u60f3\u592a\u591a', u'\u674e\u7396\u54f2', u'\u60f3\u592a\u591a'), (u'\u7f8e\u597d\u7684\u6628\u5929', u'\u80e1\u590f', u'\u66ff\u6211\u7167\u987e\u5979'), (u'\u5306\u5306\u90a3\u5e74', u'\u738b\u83f2', u'\u5306\u5306\u90a3\u5e74'), (u'\u7d20\u989c', u'\u8bb8\u5d69/\u4f55\u66fc\u5a77', u'\u4f24\u611f\u60c5\u6b4c\u5bf9\u5531'), (u'\u6211\u4e0d\u914d', u'\u5468\u6770\u4f26', u'\u6211\u5f88\u5fd9'), (u'\u771f\u5fc3\u82f1\u96c4', u'\u6210\u9f99/\u5468\u534e\u5065/\u9ec4\u8000\u660e/\u674e\u5b97\u76db', u'\u674e\u5b97\u76db (\u4e0e\u4ed6\u4eec) \u7684\u51e1\u4eba\u6b4c'), (u'\u5c0f\u9152\u7a9d (\u56fd\u8bed)', u'\u6797\u4fca\u6770/\u8521\u5353\u598d', u'JJ\u9646'), (u'\u4eb2\u7231\u7684\uff0c\u90a3\u4e0d\u662f\u7231\u60c5', u'\u5f20\u97f6\u6db5', u'Ang 5.0'), (u'\u9047\u89c1', u'\u5b59\u71d5\u59ff', u'The Moment'), (u'\u6700\u719f\u6089\u7684\u964c\u751f\u4eba', u'\u8427\u4e9a\u8f69', u'\u8427\u4e9a\u8f69 \u540c\u540d\u4e13\u8f91'), (u'\u5f69\u8679', u'\u5468\u6770\u4f26', u'\u6211\u5f88\u5fd9'), (u'\u7231\uff0c\u5f88\u7b80\u5355', u'\u9676\u5586', u'\u539f\u6c41\u539f\u5473-2005\u8d85\u5973\u7ffb\u5531\u7bc7'), (u'\u5014\u5f3a', u'\u4e94\u6708\u5929', u'\u77e5\u8db3 \u6700\u771f\u6770\u4f5c\u9009'), (u'\u4ee5\u540e\u7684\u4ee5\u540e', u'\u5e84\u5fc3\u598d', u'\u5e84\u5fc3\u598d\u60c5\u6b4c\u7cbe\u9009\u96c6'), (u'\u5e73\u51e1\u4e4b\u8def', u'\u6734\u6811', u'\u730e\u6237\u661f\u5ea7'), (u'\u6d77\u7ef5\u5b9d\u5b9d', u'\u56de\u97f3\u54e5', u'\u56de\u97f3Echo'), (u'\u5927\u6d77', u'\u5f20\u96e8\u751f', u'\u5927\u6d77'), (u'\u60f3\u5531\u5c31\u5531', u'TFBOYS', u'\u6211\u5c31\u662f\u6211 \u7535\u5f71\u539f\u58f0\u5e26'), (u'\u5343\u91cc\u4e4b\u5916 (\u72ec\u5531\u7248)', u'\u8d39\u7389\u6e05', u'\u56de\u60f3\u66f2 \u9752\u9752\u6821\u6811'), (u'\u5168\u4e16\u754c\u5ba3\u5e03\u7231\u4f60', u'\u5b59\u5b50\u6db5/\u674e\u6f47\u6f47', u'\u4e00\u5e74\u4e00\u5ea6\u7684\u590f\u5929'), (u'\u5979\u8bf4', u'\u6797\u4fca\u6770', u'\u5979\u8bf4 \u6982\u5ff5\u81ea\u9009\u8f91'), (u'\u950b\u5473', u'\u8c22\u9706\u950b', u'\u6211\u5b58\u5728'), (u'\u70df\u82b1\u6613\u51b7', u'\u5468\u6770\u4f26', u'\u8de8\u65f6\u4ee3'), (u'\u660e\u660e\u5c31', u'\u5468\u6770\u4f26', u'\u5341\u4e8c\u65b0\u4f5c'), (u'\u7ea2\u5c18\u5ba2\u6808', u'\u5468\u6770\u4f26', u'\u5341\u4e8c\u65b0\u4f5c'), (u'\u4e03\u79d2\u949f\u7684\u8bb0\u5fc6', u'\u5f90\u826f/\u5b59\u7fbd\u5e7d', u'\u60c5\u8bdd'), (u'\u8001\u7537\u5b69', u'\u7b77\u5b50\u5144\u5f1f', u'\u7236\u4eb2'), (u'\u653e\u751f', u'\u8303\u9038\u81e3', u'\u4e0d\u8bf4\u51fa\u7684\u6e29\u67d4')]
        self.maxDiff = None
        self.assertEqual(l, res)

if __name__ == '__main__':
    unittest.main()
