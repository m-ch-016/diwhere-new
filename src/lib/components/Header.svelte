<script>
  import HeaderButton from "./HeaderButton.svelte";
  import Navbar from "./Navbar.svelte";

  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();
  const loginclicked = () => {
    console.log("bababa");
    dispatch("login");
  };
</script>

<header>
  
  
  <Navbar link='/'>Home</Navbar>
  <a href="/" class="logo"><h1>DIWhere</h1></a>
  <!-- <div class="headerbutton">
    <HeaderButton />
  </div> -->
  <Navbar link='/brands'>Brands</Navbar>
</header>

<style>
  /* .headerbutton {
    color: black;
  } */
  header {
    display: flex;
    justify-content: space-between;
    padding: 1.5rem;
    align-items: center;
    color: hsl(48, 100%, 50%);
    background-color: #004735;
  }

  .logo {
    font-size: 3rem;
    font-weight: 700;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  Navbar {
    color: hsl(48, 100%, 50%);
  }
</style>
