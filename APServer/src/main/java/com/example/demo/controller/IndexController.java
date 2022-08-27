package com.example.demo.controller;

import org.springframework.web.bind.annotation.RequestParam;
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

    @GetMapping(value = {"/map", ""})
    public String map(@RequestParam("x") String x, @RequestParam("y") String y, Model model) {
        model.addAttribute("x", x);
        model.addAttribute("y", y);
        return "map";
    }


}
