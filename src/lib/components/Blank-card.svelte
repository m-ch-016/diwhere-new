<div class="category-card blank-card">
    <div class="circle" />
    <div class="content">
        <h2>Heating</h2>
        <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam
            harum obcaecati nulla, quod vel atque corporis ad est fuga doloribus
            ut ex molestiae!
        </p>
    </div>
    <img src="heating.png" alt="" />
</div>

<style>
     p, h2 {
        color: black;
    }
    
    .category-card {
        display: flex;
        margin-top: 3rem;
        margin-left: 3rem;
        margin-right: 3rem;
        margin-bottom: 3rem;
        position: relative;
        width: 500px;
        height: 275px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        border-radius: 20px;
        transition: 0.5s;
    }

    .blank-card {
        opacity: 0;
    }

    .category-card .circle {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 30px;
        overflow: hidden;
    }

    .category-card .circle::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #02585f;
        clip-path: circle(80px at center);
        transition: 0.5s;
    }

    .category-card:hover .circle::before {
        clip-path: circle(400px at center);
        background: #ffcb00;
    }

    .category-card img {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        height: 100px;
        pointer-events: none;
        transition: 0.5s;
    }

    .category-card:hover img {
        left: 80%;
        height: 275px;
    }

    .category-card:hover::after {
        border-radius: 20px;
    }

    .category-card .content {
        position: relative;
        width: 50%;
        padding: 10px 10px 10px 20px;
        transition: 0.5s;
        opacity: 0;
        visibility: hidden;
    }

    .category-card:hover .content {
        left: 0;
        opacity: 1;
        visibility: visible;
    }

    .category-card .content h2 {
        text-transform: uppercase;
        font-size: 2em;
        line-height: 1em;
        padding-bottom: 2.5rem;
    }

    .category-card .content p {
        transform: translateY(-30px);
    }

</style>