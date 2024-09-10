<script>

    import Sidebar from "../../components/Sidebar.svelte"


    let htmlContent = '';

  // Fetch the HTML content
  fetch('src/graphs/graphs/graph.html')
    .then(response => response.text())
    .then(html => {
      htmlContent = html;
    });

</script>

<Sidebar active="network"/>

<div>
    {@html htmlContent}
</div>
