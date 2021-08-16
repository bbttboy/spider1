from lxml import etree

html = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热1</nick>
        </div>
        <div>
            <nick>热热热热2</nick>
            <div>
                <nick>热热热热3</nick>
            </div>
        </div>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppj">胖胖姐</nick>
    </partner>
</book>
"""

tree = etree.XML(html)
# result = tree.xpath("/book/name")  # /表示层级关系，第一个/是根节点， 返回list列表
# result = tree.xpath("/book/name/text()")  # text() 拿文本
# result = tree.xpath("/book/author//nick/text()")  # // 后代
# result = tree.xpath("/book/author/*/nick/text()")  # * 任意的节点，通配符
result = tree.xpath("/book//nick/text()")

# print(type(result))
print(result)
