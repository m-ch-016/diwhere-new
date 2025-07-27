<div class="category-card">
  <div class="circle" />
  <div class="content">
    <h2>Bathroom</h2>
    <p>
      Here we offer a wide range of bathroom equipment. From
      toilets to showerheads, we have everything you need to create the bathroom
      of your dreams. We also have a selection of vanities, mirrors, cabinets,
      and lighting fixtures to help complete the look of your space. Happy DIY-ing!
    </p>
  </div>
  <img src="bathroom.png" alt="" />
</div>

<style>
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
    overflow: hidden;
  }
  
  .category-card:hover .circle::before {
    clip-path: circle(400px at center);
    background: #ffcb00;
    transition: 0.5s ease-in-out;
    overflow: hidden;
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
    transition: 0.5s ease-in-out;
    opacity: 0;
    visibility: hidden;
    overflow: hidden;
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
