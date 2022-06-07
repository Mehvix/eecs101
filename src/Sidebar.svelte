<script>
    // todo search include answer contents, give weights
    export let filteredPosts;
    $: filteredPosts = () => {
        return filter
            ? posts.filter(
                  (post) =>
                      post.subject
                          .toLowerCase()
                          .includes(filter.toLowerCase()) || post.nr === +filter
              )
            : posts;
    };

    export let selected;
    export let posts;
    export let filter = "";
</script>

<div id="sidebar">
    <div id="search-box">
        <input
            class="search"
            placeholder="Search"
            type="text"
            bind:value={filter}
        />
    </div>
    <div class="container">
        {#each filteredPosts() as post}
            <div
                class="post"
                class:selected={post.nr === selected}
                on:click={() => (selected = post.nr)}
                on:click={() => (window.location.hash = post.nr)}
            >
                <span class="head">
                    <span class="title">{@html post.subject}</span>
                    <div class="timestamp">
                        {@html new Date(post.created).toLocaleDateString()}
                    </div>
                </span>
                <span class="preview">
                    {@html post.content.slice(0, 164).replace(/<[^>]*>?/gm, "")}
                </span>
            </div>
        {/each}
    </div>
</div>

<style>
    #sidebar {
        width: 300px;
    }

    #search-box {
        background-color: #aaaaaa;
        padding: 5px;
    }

    .container {
        height: calc(100vh - 40px - 40px);
        overflow-y: scroll;
        border-right: 1px solid #eeeeee;
    }

    .preview {
        color: #80858a;
        margin-top: 3px;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .head {
        display: flex;
        justify-content: space-between;
    }

    .title {
        max-width: 200px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .timestamp {
        color: #888;
        font-size: 90%;
        height: 16px;
        line-height: 16px;
        margin-bottom: 3px;
        text-align: right;
        display: block;
        width: fit-content;
        float: right;
    }
    .post {
        overflow: hidden;
        flex-direction: column;
        display: flex;
        border-bottom: 1px solid #eeeeee;
        height: 60px;
        padding: 8px 12px;
        cursor: pointer;
        font-size: smaller;
        font-weight: 600;
    }
    .post:hover {
        background-color: #fafafa;
    }

    .selected,
    .selected:hover {
        background: #fff7ce;
    }

    .search {
        box-sizing: border-box;
        height: 30px;
        padding: 0 16px;
        margin: 0;

        color: #495057;
        display: block;
        width: 100%;
        font-size: 0.8125rem;
        line-height: 1.5;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: 0.25rem;
    }

    .search:focus {
        color: #495057;
        background-color: #fff;
        border-color: #91b8d7;
        outline: 0;
        box-shadow: 0 0 0 0.2rem rgb(62 122 171 / 25%);
    }
</style>
