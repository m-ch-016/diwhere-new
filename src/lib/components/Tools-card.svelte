<a href="/">
  <div class="category-card tools-card">
    <div class="circle" />
    <div class="content">
      <h2>Tools</h2>
      <p>
        Here we offer everything you need to get the job done right.
        From basic hand tools to more advanced power tools, we have it all on
        hand-level and power tools for work and home projects. We also offer a
        variety of tool storage options to help you keep your workshop
        organized. Happy DIY-ing!
      </p>
    </div>
    <img src="toolbox.png" alt="" />
  </div>
</a>

<style>
  p,
  h2 {
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
    background: #004735;
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

  .tools-card:hover img {
    left: 80%;
    height: 285px;
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
    padding-top: 2.5rem;
  }

  .category-card .content p {
    transform: translateY(-30px);
  }
</style>
