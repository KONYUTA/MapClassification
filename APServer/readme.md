## ビルド手順
1. Springアプリケーションの雛形を作成
    [Spring Initializr](https://start.spring.io/)にアクセス
    各項目を以下のように設定
    - Project: Maven Project
    - Language: Java
    - SpringBoot: 2.7.2
    - Project Metadata: 適当に
    - Packaging: jar
    - Javva: 11
    - Dependencies: Spring Web
        Spring Boot Actuator
        Thymeleaf

2. アプリケーションディレクトリに移動し、ビルド
    ```bash
    $ ./mvnw clean install
    //以下のような出力が出ればOK
    [INFO] ------------------------------------------------------------------------
    [INFO] BUILD SUCCESS
    [INFO] ------------------------------------------------------------------------
    ```
3. SpringBootの起動
    ```bash
    $ mvnw spring-boot:run
    ```
4. localhost:8080にアクセス
    この時点ではjson形式のなんかが出てればおk
    Ctrl+cのキーボード割り込みで終了できる
5. pom.xml内のproperty要素内に以下を追加
    ```xml
    <maven-jar-plugin.version>3.1.1</maven-jar-plugin.version>
    ```
6. 新規コントローラーを作成
    ```bash
    $ nvim src/main/java/com/example/demo/controller/IndexController.java
    ```
    以下はコードの例
    ```java
    package com.example.demo.controller;

    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;

    @Controller
    public class IndexController {
        @GetMapping(value = {"/", ""})
        public String index(Model model) {
            model.addAttribute("message", "ハローワールド!");
            return "index";
        }

    }
    ```
7. テンプレートの追加
    ```bash
    $ nvim src/main/resources/templates/index.html
    ```
    以下はコードの例
    ```html
    <!DOCTYPE html>
    <html lang="ja" xmlns:th="http://www.thymeleaf.org">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport"content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>index</title>
    </head>
    <body>
      <div id="app">
        <h1>index</h1>
        <p th:text="${message}">Hello World!</p>
      </div>
    </body>
    </html>
    ```
