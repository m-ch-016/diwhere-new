<script>
  import Bathstorelogo from "$lib/components/Bathstorelogo.svelte";
  import Bnqlogo from "$lib/components/Bnqlogo.svelte";
  import BrandsGrid from "$lib/components/BrandsGrid.svelte";
  import Frontlinelogo from "$lib/components/Frontlinelogo.svelte";
  import Homebaselogo from "$lib/components/Homebaselogo.svelte";
  import Jewsonlogo from "$lib/components/Jewsonlogo.svelte";
  import Rexellogo from "$lib/components/Rexellogo.svelte";
  import Screwfixlogo from "$lib/components/Screwfixlogo.svelte";
  import Selcologo from "$lib/components/Selcologo.svelte";
  import Toolstationlogo from "$lib/components/Toolstationlogo.svelte";
  import Victoriaplumlogo from "$lib/components/Victoriaplumlogo.svelte";
  import Wickeslogo from "$lib/components/Wickeslogo.svelte";
  import Woodieslogo from "$lib/components/Woodieslogo.svelte";
  import Marquee from "svelte-fast-marquee";
  import { fade, slide } from "svelte/transition";
  import { backInOut, cubicInOut, quintOut } from "svelte/easing";
  import Social from "$lib/components/Social.svelte";
  import BrandsMarquee from "$lib/components/BrandsMarquee.svelte";
</script>

<div class="section">
  <div class="box">
    <div class="box1title">
      <h1>HELLO!</h1>
    </div>
    <div class="box1content">
      Hello and welcome to D.I.WHERE! My name is Adi the Beaver, and I am the representative of this
      fine establishment. As a skilled craftsman and DIY enthusiast myself, I
      understand the importance of having the right tools and materials on hand
      for any home improvement project. That's why I've stocked this store with
      a wide variety of high-quality DIY equipment at unbeatable prices.
    </div>
  </div>

  <div class="box">
    <div class="box2content">
      Whether you're a seasoned pro or just starting out on your home
      improvement journey, we have something for everyone. We carry a wide range
      of plumbing supplies, including pipes, fittings, and seals, as well as
      electrical components like outlets, switches, and fixtures. And if you're
      looking for more advanced equipment, we have power saws, sanders, and
      drill presses to help you tackle even the most complex projects.
    </div>
    <div class="box2title">
      <h1>We're your guy!</h1>
    </div>
  </div>

  <div class="box">
    <div class="box2title byetitle">
      <h1>SEE YA!</h1>
    </div>
    <div class="box2content byecontent">
      So if you're in need of some new DIY equipment, or just looking to upgrade
      your current tools, you're at the right place. We'll be happy
      to help you find exactly what you need to get your project done with ease
      and confidence. Thanks for stopping by, and happy DIY-ing!
    </div>
  </div>

  <div class="box box3">
    <div class="box3title">
      <h1>Our Partners</h1>
    </div>
    <div class="box3content">
      <Marquee speed="40">
        <div class="logoimg">
          <Bnqlogo />
        </div>
        <div class="logoimg">
          <Bathstorelogo />
        </div>
        <div class="logoimg">
          <Frontlinelogo />
        </div>
        <div class="logoimg">
          <Homebaselogo />
        </div>
        <div class="logoimg">
          <Jewsonlogo />
        </div>
        <div class="logoimg">
          <Rexellogo />
        </div>
        <div class="logoimg">
          <Screwfixlogo />
        </div>
        <div class="logoimg">
          <Selcologo />
        </div>
        <div class="logoimg">
          <Toolstationlogo />
        </div>
        <div class="logoimg">
          <Victoriaplumlogo />
        </div>
        <div class="logoimg">
          <Wickeslogo />
        </div>
        <div class="logoimg">
          <Woodieslogo />
        </div>
        <div class="logoimg">
          <Bnqlogo />
        </div>
        <div class="logoimg">
          <Bathstorelogo />
        </div>
        <div class="logoimg">
          <Frontlinelogo />
        </div>
        <div class="logoimg">
          <Homebaselogo />
        </div>
        <div class="logoimg">
          <Jewsonlogo />
        </div>
        <div class="logoimg">
          <Rexellogo />
        </div>
        <div class="logoimg">
          <Screwfixlogo />
        </div>
        <div class="logoimg">
          <Selcologo />
        </div>
        <div class="logoimg">
          <Toolstationlogo />
        </div>
        <div class="logoimg">
          <Victoriaplumlogo />
        </div>
        <div class="logoimg">
          <Wickeslogo />
        </div>
        <div class="logoimg">
          <Woodieslogo />
        </div>
      </Marquee>
    </div>
  </div>

  <div class="bigbox">
    <div class="smallbox1">
      <div class="box4title">
        <h1>Need Help</h1>
      </div>
      <div class="box4content">
        If you got a problem, email us at: <br><br> rbrbrbrb@brbrbrbrb <br><br> 0123456779
      </div>
    </div>
    <div class="smallbox2">
      <div class="box5title">
        <h1>Follow Our Socials!</h1>
      </div>
      <div class="box5content">
        <ul>
          <li><Social link="/" icon="fa-brands fa-instagram" /></li>
          <li><Social link="/" icon="fa-brands fa-twitter" /></li>
          <li><Social link="/" icon="fa-brands fa-tiktok" /></li>
          <li><Social link="/" icon="fa-brands fa-facebook-f" /></li>
        </ul>
      </div>
    </div>
    <div class="smallbox3">
      <div class="box6title">
        <h1>Join the DIWHERE army!</h1>
      </div>
      <div class="box6content">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere dolor
        rem numquam hic repudiandae vero fugit distinctio mollitia magni! Eius
        fuga, eaque aut non voluptates voluptate beatae id delectus possimus.
      </div>
    </div>
  </div>
</div>

<style>
  .section {
    display: flex;
    flex-direction: column;
    margin-top: 7rem;
    margin-bottom: 7rem;
  }

  .box {
    padding-left: 8rem;
    padding-right: 8rem;
    padding-top: 5rem;
    padding-bottom: 5rem;
    background-color: #004735;
    display: flex;
    margin-bottom: 6rem;
    color: #ffcb00;
  }

  .box1title {
    text-transform: uppercase;
    padding-right: 0rem;
    text-decoration: underline 3px solid rgb(1, 128, 96);
    text-underline-offset: 0.25rem;
    width: 70rem;
    padding-left: 5rem;
  }

  .box2title {
    text-transform: uppercase;
    padding-left: 5rem;
    text-decoration: underline 3px solid rgb(1, 128, 96);
    text-underline-offset: 0.25rem;
    width: 70rem;
  }

  .box3 {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .box3title {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
    border-bottom: 3px solid rgb(1, 128, 96);
    margin-bottom: 3rem;
  }

  .box1content,
  .box2content,
  .box3content {
    font-size: 1.25rem;
  }

  .byecontent {
    margin-left: 5rem;
  }

  .byetitle {
    margin-right: 5rem;
  }

  .bigbox {
    padding-left: 8rem;
    padding-right: 8rem;
    padding-top: 5rem;
    padding-bottom: 5rem;
    display: flex;
    margin-bottom: 6rem;
  }

  .smallbox1,
  .smallbox2,
  .smallbox3 {
    background: #004735;
    padding: 2rem;
    display: flex;
    width: 33%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    height: 20rem;
    color: #ffcb00;
    padding: 1rem 3rem 3rem 3rem;
  }

  .smallbox1,
  .smallbox2 {
    margin-right: 0.5rem;
  }

  .smallbox2,
  .smallbox3 {
    margin-left: 0.5rem;
  }

  .box4content,
  .box5content,
  .box6content {
    margin-top: 3rem;
    font-size: 1.05rem;
  }

  .box4title,
  .box5title,
  .box6title {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
    border-bottom: 3px solid rgb(1, 128, 96);
  }

  .box5content {
    margin-top: 1rem;
    position: relative;
    width: 23.2rem;
    margin-bottom: 2rem;
    height: 10vh;
    margin-left: 2rem;
    margin-right: 2rem;
    justify-content: space-around;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    background: linear-gradient(to bottom, #004735, #004735);
  }

  .box5content::before {
    content: "";
    position: absolute;
    bottom: 0;
    width: 23.2rem;
    height: 5vh;
    z-index: 1;
    backdrop-filter: blur(5px);
  }

  .box5content ul {
    position: relative;
    display: flex;
    z-index: 2;
  }

  .box5content ul li {
    position: relative;
    list-style: none;
    margin-right: 10px;
  }

  .box3content {
    width: 110rem;
    overflow: hidden;
  }

  .logoimg {
    margin-right: 2rem;
    margin-left: 2rem;
  }
</style>
