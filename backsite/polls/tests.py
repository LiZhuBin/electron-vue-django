import models


def date_change():
    """将数据库数据修改、清洗后存入change_date数据仓库中"""
    object = None
    for date in models.OriOrders.objects.all():
        object = models.ChangeDates(year=str(date.bookdate).split("-")[0], month=str(date.bookdate).split("-")[1],
                                    day=str(date.bookdate), id=date.id)
        object.save()

if __name__ == '__main__':
    date_change()