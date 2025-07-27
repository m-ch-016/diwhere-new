<div class="brands-card">
    <div class="circle" />
    <div class="content">
        <h2>Homebase</h2>
        <p>
            With over 150 stores and 5,600 team members across the UK and
            Ireland, we're here to bring your homes and gardens to life. From
            gardening, decorating, and home furnishing, we've got it
            all - from kitchens to bathrooms, we have everything you need.
        </p>
    </div>
    <img src="homebaselogo.png" alt="" />
</div>

<style>
    .brands-card {
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

    h2 {
        margin-top: 2rem;
    }
    .brands-card .circle {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 30px;
        overflow: hidden;
    }

    .brands-card .circle::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #004735;
        clip-path: circle(80px at center);
        transition: 0.5s;
    }

    .brands-card:hover .circle::before {
        clip-path: circle(400px at center);
        background: #ffcb00;
    }

    .brands-card img {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        height: 50px;
        width: 250px;
        pointer-events: none;
        transition: 0.5s;
    }

    .brands-card:hover img {
        left: 85%;
        height: 75px;
        width: 340px;
    }

    .brands-card:hover::after {
        border-radius: 20px;
    }

    .brands-card .content {
        position: relative;
        width: 50%;
        padding: 10px 10px 10px 20px;
        transition: 0.5s;
        opacity: 0;
        visibility: hidden;
    }

    .brands-card:hover .content {
        left: 0;
        opacity: 1;
        visibility: visible;
    }

    .brands-card .content h2 {
        text-transform: uppercase;
        font-size: 2em;
        line-height: 1em;
        padding-bottom: 2.5rem;
    }

    .brands-card .content p {
        transform: translateY(-30px);
    }
</style>
