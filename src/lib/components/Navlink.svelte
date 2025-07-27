<script>
  // export let link;
</script>

<div>
  <slot />
</div>

<style>
  div {
    color: inherit;
    text-decoration: none;
    position: relative;
    z-index: 0;
    font-size: 1.25rem;
    padding: 0.5rem 1rem;
    transition: color 0.5s;
    border-radius: 1rem;
    overflow: hidden;
    
  }

  div::after {
    content: "";
    height: 0;
    width: 100%;
    position: absolute;
    left: 0;
    bottom: 0;
    background-color: #ffcb00;
    z-index: -1;
    transition: 0.5s;
  }

  div:hover {
    font-weight: 600;
    box-shadow: 0px 2px black;
    color: black;
  }

  div:hover::after {
    height: 100%;
  }
</style>
