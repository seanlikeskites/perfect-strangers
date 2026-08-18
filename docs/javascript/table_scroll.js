document$.subscribe(function() {
    tables = document.querySelectorAll(".centre-table")

    for (const tab of tables){
        vertical_title = tab.querySelector(".vertical-title");
        row_title = tab.querySelector(".row-title");

        title_left = `${vertical_title.offsetWidth + row_title.offsetWidth}px`
        horizontal_title = tab.querySelector(".horizontal-title");
        horizontal_title.style.left = title_left;

        inner_table = tab.querySelector("table");
        margin = window.getComputedStyle(inner_table)["margin-right"];

        table_width = `${vertical_title.offsetWidth + row_title.offsetWidth + horizontal_title.offsetWidth + parseInt(margin, 10)}px`;
        tab.style.maxWidth = table_width;
    }
})
