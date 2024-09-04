<script>
    import "../style.css"
    export let active;

</script>

<style>

.sidebar {
    padding: 0;
    width: 120px;
    background-color: var(--lightGrey);
    position: fixed;
    height: 100%;
    overflow: auto;
    z-index: 1000;
  }

  .menuLabel {
    text-align: center;
    margin-bottom: 5px;
    text-decoration: underline;
  }

  .home {
    margin-top: 100px;
    margin-bottom: 100px;
  }

  .icon_border {
    height: 30px;
    width: 50px;
    margin:auto;
    border-radius: 10px;

  }

  .icon {
    margin-top: 4px;
  }
  
  /* Sidebar links */
  .sidebar a {
    display: block;
    color: black;
    padding: 8px;
    text-decoration: none;
    text-align: center;

  }
  
  /* Active/current link */
  .sidebar a.active {
    background-color: var(--emhs1);
    color: white;
  }
  
  /* Links on mouse-over */
  .sidebar a:hover:not(.active) {
    background-color: var(--emhsGrey3);
    color: white;
  }

  .cls-1 {
                      fill: none;
                    }

  

</style>


<div class="sidebar">
    <a class="link home {active == "" ? "active" : ""}" href="/">
      <div>Home</div>
    </a>

    <a class="link {active == "options" ? "active" : ""}" href="options">
        <div>LJS</div></a>

    <a class="link {active == "plots" ? "active" : ""}" href="plots">
        <div>Plots</div></a>

    <a class="link {active == "network" ? "active" : ""}" href="network">
        <div>Network</div></a>

    <a class="link {active == "matching" ? "active" : ""}" href="matching">
        <div>Matching</div></a>

</div>