# summernote_Nestable_flask
summernote Combine Nestable Use Python Flask

* [Demo](https://youtu.be/UhjntU5Ql4U)  

搭配 SQLite 簡單的結合 [Summernote](http://summernote.org/) 以及超酷炫的 [Nestable](http://dbushell.github.io/Nestable/)
 
## 特色
* 強大的 [Summernote](http://summernote.org/) 。
* 超酷炫的 [Nestable](http://dbushell.github.io/Nestable/)。

## 執行說明
請先確定電腦有安裝 [Python](https://www.python.org/)

接著使用下列指令即可運行
``` 
python app.py
```

## 執行畫面
可輸入Title(標題)、 Sequence(排序)、 Content(內文)，輸入完按右下角的 + 即可，如下圖。

![alt tag](http://i.imgur.com/22yy6zS.jpg)

這部分顯示您輸入過的資料(可編輯 or 修改 or 刪除)，如下圖。

![alt tag](http://i.imgur.com/AzvxTSD.jpg)

這部分則是超酷炫的Nestable，可以去任意切換他的順序，顯示的效果會在Preview裡面呈現，

目前我只設定他為一層而已，如下圖。

![alt tag](http://i.imgur.com/8HkyCv3.jpg)

為什麼目前 Nestable 我只設定為一層而已，因為多層(children)可能需要用到 <b>遞迴(recursion) </b> 的概念，所以暫時只用一層，

等我哪天想通了我再來修改XDDDD

最後的 Preview 則是顯示設定過的資料(如下圖)，按照你設定的排序(數字越小的排的越前面)。

![alt tag](http://i.imgur.com/4jN7rYT.jpg)


## External JS
* [Summernote](http://summernote.org/)
* [Nestable](http://dbushell.github.io/Nestable/)
* [DataTables](https://datatables.net/)

## 執行環境
* Python 3.5.2

## License
MIT license
