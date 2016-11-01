from django.shortcuts import render

class CheckSourceMiddleWare(object):
    def process_request(self,request):
        from_source = request.META['HTTP_USER_AGENT']

        #ie9以下的浏览器，都是Mozilla/4.0的，ie9及以上版本是Mozilla/5.0，
        #故采取此方式判断，感觉这种方式也是最简单的
        if 'Mozilla/5.0' not in from_source:
            return render(request,'ie_update.html')

