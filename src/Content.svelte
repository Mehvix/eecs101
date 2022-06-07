<script>
    import Comment from "./Comment.svelte";
    import Text from "./Text.svelte";

    export let question;
    $: question = post.history[0];

    export let subject;
    $: subject = question.subject;

    export let content;
    $: content = question.content;

    export let views;
    $: views = post.unique_views;

    export let tags;
    $: tags = post.tags;

    export let studentAnswer;
    $: studentAnswer = post.children.find((child) => child.type === "s_answer");

    export let instructorAnswer;
    $: instructorAnswer = post.children.find(
        (child) => child.type === "i_answer"
    );

    export let comments;
    $: comments = post.children.filter((child) => child.type === "followup");

    // fix w non-anon
    function studentName(students) {
        return post.anon !== "no"
            ? "Anonymous"
            : (students[post.uid] || { name: "Anonymous" }).name;
    }
    export let post;
    export let students;
</script>

<div class="content">
    <!-- todo doesn't catch if invalid/non-existing -->
    {#if post}
        <div id="question">
            <div id="head">
                <h1>{@html subject}</h1>
                <div id="views">
                    <span class="count">{@html views}</span> views
                </div>
            </div>
            <main>
                <Text input={content} />
                <!-- todo make tags search onclick -->
                <div id="tags">
                    {#each tags as tag}
                        <span>
                            <a>{tag}</a>
                        </span>
                    {/each}
                </div>
            </main>
            <div class="author">
                <span>
                    Good question ({(post.tag_good || []).length})
                </span>
                <span>
                    {studentName(question)}
                </span>
            </div>
        </div>

        {#if studentAnswer}
            <div class="answer">
                <h2>Student Answer</h2>
                <article>
                    <Text input={studentAnswer.history[0].content} />
                </article>
                <div class="author">
                    <span>
                        Thanks! ({(studentAnswer.tag_endorse || []).length})
                    </span>
                    <span>
                        {studentName(studentAnswer.history[0])} on {@html new Date(
                            post.created
                        ).toLocaleString()}
                    </span>
                </div>
            </div>
        {/if}

        {#if instructorAnswer}
            <div class="answer">
                <h2>Instructors Answer</h2>
                <article>
                    <Text input={instructorAnswer.history[0].content} />
                </article>
                <div class="author">
                    {studentName(instructorAnswer)}
                </div>
            </div>
        {/if}

        <div id="comments">
            {#each comments as comment}
                <Comment {comment} {students} />
            {/each}
        </div>
    {:else}
        No post is selected
    {/if}
</div>

<style>
    h1,
    h2 {
        margin: 0;
    }

    #head {
        display: flex;
        justify-content: space-between;
    }

    #views {
        height: 22px;
        color: white;
        font-weight: normal;
        border-radius: 3px;
        background-clip: padding-box;
        padding: 1px 6px 0;
        text-shadow: #0a0a0a 0px 1px 0px;
        background: #555;

        font-size: 14px;
        line-height: 1.7;

        min-width: fit-content;
        margin-left: 12px;
    }

    .count {
        font-size: 16px;
        line-height: 1.3;
        margin-right: 5px;
        font-weight: bold;
    }

    #tags {
        margin-top: 1em;
    }

    #tags span {
        color: #448ab6 !important;
        background: #d1e8f1 !important;

        cursor: pointer;
        display: inline-block;
        font-size: 10px;
        line-height: 12px;
        padding: 5px 7px;
        border-radius: 3px;
        background-clip: padding-box;
        text-shadow: none;
        border: none;
        background: #efefef;
        color: #777;
        margin-right: 2px;
        margin-bottom: 2px;
    }

    #tags > span:hover {
        text-decoration: none;
        background: #448ab6 !important;
        color: white !important;
    }

    #tags a {
        text-decoration: none;
        color: inherit !important;
    }

    .content {
        box-sizing: border-box;
        flex-grow: 1;
        padding: 0 32px;
        height: calc(100vh - 40px);
        overflow-y: scroll;
        background-color: #eaeff4;
    }

    .content > div {
        background-color: #ffffff;
        border-radius: 5px;
        box-shadow: 0 0 3px #676869;
    }

    .author {
        color: #666;
        font-size: smaller;
        text-align: right;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        background-color: #f6f7f6;
        background-clip: content-box;
        height: 32px;
        align-items: center;
        border-top: 1px solid #eaecee;
    }

    .author * {
        margin: 8px;
    }

    #question,
    .answer {
        border: 1px solid #eeeeee;
        margin: 16px 0;
    }

    #question > :not(.author),
    .answer > :not(.author) {
        margin: 16px 24px;
    }

    #comments,
    #question,
    .answer {
        box-sizing: border-box;
        max-width: 710px;
    }
</style>
