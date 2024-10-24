#### dataclass注解

Java 的 @Data 注解（通常使用 Lombok 库提供）会自动生成 getter、setter、toString、equals、hashCode 等方法，使得类的定义更加简洁。

Java 的 record 关键字（从 Java 14 开始引入）用于创建不可变数据对象，并自动生成构造方法、equals、hashCode、toString 等方法，适用于需要简单存储数据的场景。

Python 的 @dataclass 也能自动生成类似的功能，包括 __init__、__repr__、__eq__ 等方法，简化类的定义，特别是用于定义数据结构时。