---
# the default layout is 'page'
icon: fas fa-info-circle
order: 5
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .gallery {
            column-count: 2; /* 设置列数 */
            column-gap: 10px; /* 设置列之间的间隙 */
        }
        .gallery img {
            width: 100%;
            break-inside: avoid; /* 避免图片跨列显示 */
            margin-bottom: 10px; /* 设置图片之间的间隙 */
        }
    </style>
</head>
<body>

<div class="gallery">
    <img src="{{site.url}}/assets/DSCF3374.jpg" alt="Photo 1">
    <img src="{{site.url}}/assets/IMG_4536.jpg" alt="Photo 2">
    <img src="{{site.url}}/assets/DSCF3450.jpg" alt="Photo 3">
    <img src="{{site.url}}/assets/DSCF3488.jpg" alt="Photo 4">
    <img src="{{site.url}}/assets/DSCF3745.jpg" alt="Photo 5">
    <!-- 更多图片 -->
</div>

</body>




