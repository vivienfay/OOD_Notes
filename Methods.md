# OOD基础
- access modifier
  - protected: 开放给 我自己 + 子类
  - public: 开放给 所有人
  - private: 开放给 我自己
  - override: 重写父类函数
  - overlode: input args不同 重载
- 封装 encapsulation
    ```java
    class Animal {}
    Animal a = new Animal();
    class Dog extned
    ```
- 继承 inheritence
    ```java
    class Dog extends Animal {}
    ```
    protected, public可以继承， 可以override或者overload

- 多态 polymorphism
    ```Java
    abstract class Animal{
        public abstract void makeSound();
    }
    final class Dog extends Animal{
        public void makeSound(){
            System.out.println('Woof!')
        }
    }
    final class Cat extends Animal{
        public void makeSound(){
            System.out.println('Meeow!')
        }
    }
    Animal animal1 = new Dog();
    Animal animal2 = new Cat();
    <!-- 会有不同的表现 -->
    animal1.makeSound();
    animal2.makeSound();
    ```
- Example: 
    ```java
    class Animal {
        public void description(){
            System.out.println("A general Animal Object")
        }
        protected String name; // 子类可以继承
        private String privacy; //只能自己用
        public int id; //所有都有access
    }

    Animal a = new Animal();
    class Dog extends Animal {}; //继承
    Dog dog = new Dog();
    dog.description();

    class Cat extends Animal {
        //overide
        public void description(){
            System.out.println("A cat Object")
        }
    }

    class Bear extends Animcal {
        public void description(){
            super(); // call the base class's description
        }
    }
    ```

    ```java
    abstract class Animal{}
    class Dog extends Animal{}
    Animal animal = new Animal(); //this is wrong
    Dog dog = new Dog(); // this correct
    ```

    Interface 像是方法的集合，没有constructor
    ```Java
    interface Service{
        // No constructor
        public void serve();
        public void retire();
    }

    class Dog implements Service{
        public void serve()
        pbulic void retire()
    }
    ```

- Exception
  - Checked Exception(10 Exception, compile time exception)
  - Unchecked Exception(Runtime Exception, NPE)
  ```Java
  class MyException extends Exception{ //继承系统的exception
      public MyExcpetion(String s){
          super(s);
      }
  }

  public class Testing{
      public void test(){
          try{
              throw new MyException("My exception");
          }
          catch (MyException ex){
              System.out.println(ex.getMessage());
          }
      }
  }
  ```

- Enum
  
  ```Java
  public enum TrafficSignal{
      RED, YELLOW, GREEN
  }
  public class Testing{
      TrafficSignal signal = new TrafficSignal.RED;
  }
  ```

# 面试分析方法
- Clarify: 去除歧义， 确定答题范围
  - What: 题目关键字，属性，特点，功能
  - How: 功能
  - Who: 谁在使用
- Core Object: 确定题目所涉及的类，以及类之间的映射关系
  - Package:  如果什么都不声明， 变量和函数都是package level visible的，在同一个package内的其他类
  - Public: 如果声明是public，变量和函数都是public level visible的， 任何其他的类都可以访问（+）
  - Private: 如果声明是private，变量和函数都是class level visible的，仅有定义这些变量和函数的类自己可以访问（封装）
  - Protected: 如果声明是protected，变量和函数在能被定义他们的类访问的基础上，还能被该类的子类所访问（继承）（#）
- Cases: 确定题目中所需要实现的场景和功能
	- 要实现的功能放在白纸黑字上use cases
- Class(UML类图): 通过类图的方式，具体填充题目中涉及的类
	- 遍历你所列出的use cases
	- 对于每个use case 更加详细描述use case在做什么事情
	- 针对这个描述，在已有的core objects里填充进所需要的信息
- Correctness: 检查自己的设计，是否满足关键点


# OOD原则 - SOLID

1. S - Single responsibility principle 单一责任原则
   
   一个类应该有且只有一个去改变他的理由，一个类应该只有一项工作
2. O - Open close principle 开放封闭原则

    对象或实体应该对扩展开放，对修改封闭，open to extension, close to modification

3. L - Liskov subsitution Principle 里氏替换原则
   
    任何一个子类或派生类应该可以替换他们的基类或父类

4. I - Interface segregation Principle 接口分离原则
   
   不应该强迫一个类实现它用不上的接口
   
5. D - Dependency Inbersion Principle 依赖反转原则
   
   抽象不应该依赖于具体实现，具体实现应该依赖于抽象


# Good Practice

1. Raise Exception