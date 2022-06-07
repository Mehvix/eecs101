<script>
    export let title;
</script>

<header>{title}</header>
<div class="spacer" />

<style>
    header {
        height: 40px;
        width: 100%;
        background-color: #3e7aab;
        color: white;
        font-size: larger;
        font-weight: bold;
        display: flex;
        align-items: center;
        padding: 0 16px;
        position: fixed;
    }
    .spacer {
        height: 40px;
    }
</style>
