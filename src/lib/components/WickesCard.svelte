<div class="brands-card">
    <div class="circle" />
    <div class="content">
        <h2>Wickes</h2>
        <p>
            40 years of delivering outstanding value for money has been the
            cornerstone of our success. We take pride in being an innovative and
            multi-channel retailer. Customers have access to a range of How To
            guides, ideas and advice to support them with their home improvement
            projects.
        </p>
    </div>
    <img src="wickeslogo.png" alt="" />
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
        height: 70px;
        pointer-events: none;
        transition: 0.5s;
    }

    .brands-card:hover img {
        left: 75%;
        height: 140px;
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
