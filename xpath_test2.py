from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath("/html")
# result = tree.xpath("/html/body/ul/li/a/text()")
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的顺序是从1开始的，[]表示索引
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # [@xxx=xxx] 属性的筛选

# print(result)

# ol_li_list = tree.xpath("/html/body/ol/li")
#
# for li in ol_li_list:
#     result = li.xpath("./a/text()")
#     print(result)
#     result2 = li.xpath("./a/@href")  # 拿到属性值： @属性
#     print(result2)
#
# print(tree.xpath("/html/body/ul/li/a/@href"))

print(tree.xpath("/html/body/div[1]/text()"))
