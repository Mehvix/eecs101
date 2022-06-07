<script>
    import katex from "katex";
    import he from "he";

    // todo fix scrolling issue caused by katex
    // todo catch replies i.e. @17057_f8
    export let rendered;
    $: rendered = () => {
        input = input.replace(/\$\$([^$]+)\$\$/g, (eq) => {
            return katex.renderToString(he.decode(eq.slice(2, -2)));
        });
        input = input.replace(/&#64;(\d+)/g, `<a href=#\$1>@\$1</a>`);
        return input;
    };

    export let input;
</script>

<div>
    {@html rendered()}
</div>

<style>
    div {
        color: #333;
    }
</style>
