<script>

    import Sidebar from "../../components/Sidebar.svelte"
    import { onMount } from 'svelte';

    let htmlContent = '';

    onMount(() => {
    // Fetch the external HTML file
    async function fetchHtml() {
        const response = await fetch('/graph_big.html');
        htmlContent = await response.text();
    }

    // Call the function to load the content on mount
    fetchHtml();
    });
    
    let contentDiv;

    

    // Inject the HTML content after it's fetched
    $: if (contentDiv && htmlContent) {
        contentDiv.innerHTML = htmlContent;
    }

</script>
<Sidebar active="network"/>
<main>
    <div class="content" bind:this={contentDiv}></div>
</main>


