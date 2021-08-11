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
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppj">胖胖姐</nick>
    </partner>
</book>
"""