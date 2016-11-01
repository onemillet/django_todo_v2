from django import template
from datetime import datetime

register = template.Library()

def format_time(var):
    create_time=var.create_time
    now=datetime.now()
    #print(type(create_time))
    #print(type(now))
    #需做如下转化，否则2个时间相减会报错
    create_time=create_time.replace(tzinfo=None)
    #获得相差的总秒数
    result=(now-create_time).total_seconds()
    #print(result)
    #print(now)

    minutes = int(result/60)
    if minutes <60:
        content = var.content + u'——发布于%s分钟前' % (minutes)
        return content

    hours = int(result/3600)

    if hours < 24:
        content=var.content+u'——发布于%s小时前'%(hours)
        return content
    else:
        days = int(hours/24)
        if days < 7:
            content=var.content+u'——发布于%s天前'%(days)
            return content
        else:
            weeks = int(days/7)
            if weeks < 5:
                content = var.content + u'——发布于%s周前' % (weeks)
                return content
            else:
                content = var.content + u'——发布于%s周前' % (int(weeks/4))
                return content

register.filter(name='format_time',filter_func=format_time)