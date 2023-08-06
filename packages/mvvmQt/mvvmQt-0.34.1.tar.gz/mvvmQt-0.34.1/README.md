<!-- 
python setup.py sdist
twine upload dist/* 
-->

# 简介
使用mvvmQt可以方便的使用jinja2的模板创建Qt界面，并且提供了mvvm的方式来进行数据操作和展示，提高开发速度。

# 控件
## 1. 窗体
### Widget、Window
> 使用Widget可以创建一个普通窗体，Window则在Widget的基础上提供更好的可视化操作，具体可参考Qt的介绍

```html
<app>
    <window>
        <attr-minWidth v="{{ (desktop.width() * 2 / 3) | round | int }}" />
        <attr-minHeight v="{{ (desktop.height() * 2 / 3) | round | int }}" />
        <attr-maxWidth v="{{ desktop.width() }}" />
        <attr-maxHeight v="{{ desktop.height() }}" />
        <attr-title ob="spacing" format="Grid Spacing: %d" />
        <attr-pos v="200, 200" />
    </window>
</app>
```

## 1. 布局
### Grid
