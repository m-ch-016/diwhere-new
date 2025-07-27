<script>
  export let link;
  export let icon;
</script>

<a href={link}><i class="fa-brands {icon}" /></a>

<style>
  a {
    position: relative;
    width: 80px;
    height: 80px;
    display: inline-block;
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: #fff;
    font-size: 2em;
    box-shadow: 0 5px 45px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(2px);
    transition: 0.5s;
    overflow: hidden;
  }

  i {
    margin-top: 50%;
    height: 100%;
  }

  a:hover {
    transform: translateY(-20px);
  }

  a::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 50px;
    height: 100%;
    /* background: rgba(255, 255, 255, 0.5); */
    background-color: #ffcb00;
    transform: skewX(45deg) translateX(150px);
    transition: 0.5s;
  }

  a:hover::before {
    transform: skewX(45deg) translateX(-150px);
  }
</style>
