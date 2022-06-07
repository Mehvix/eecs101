<script>
    import Text from "./Text.svelte";

    export let comment;
    export let students;

    // todo fix for non-anon
    function studentName(post) {
        return post.anon !== "no"
            ? "Anonymous"
            : (students[post.uid] || { name: "Anonymous" }).name;
    }
</script>

<div class="comment">
    <div class="author">
        {studentName(comment)}
    </div>
    <Text input={comment.subject} />

    {#each comment.children as response}
        <div class="response">
            <div class="author">
                {studentName(response)}
            </div>
            <Text input={response.subject} />
        </div>
    {/each}
</div>

<style>
    .author {
        color: #666;
        font-size: smaller;
    }

    .comment,
    .response {
        box-sizing: border-box;
        padding: 16px;
        margin: 16px 0;
        border: 1px solid #eeeeee;
        width: 100%;
    }
</style>
