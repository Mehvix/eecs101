<script>
    import ALL_POSTS from "../cs348-fall-2017.json";

    ALL_POSTS.sort((a, b) => b.result.nr - a.result.nr);

    function getStudents() {
        const students = [].concat(
            ...posts.map((post) =>
                [].concat(
                    post.tag_good || [],
                    post.tag_endorse || [],
                    getStudents(post.children)
                )
            )
        );
        console.log(students);
        const ids = new Set();

        for (const student of students) {
            const { id } = student;
        }

        return students.filter((id) => {
            if (ids.has(id)) {
                return false;
            }
            ids.add(id);
            return true;
        });
    }

    import Header from "./Header.svelte";
    import Sidebar from "./Sidebar.svelte";
    import Content from "./Content.svelte";

    export let titles;
    $: titles = posts.map(
        ({ nr, created, history: [{ subject, content }] }) => ({
            nr,
            subject,
            content,
            created,
        })
    );

    export let students;
    $: students = () => {
        return getStudents(posts).reduce(
            (acc, student) => Object.assign(acc, { [student.id]: student }),
            {}
        );
    };

    export let selected = parseInt(window.location.hash.slice(1)) || 1;

    onhashchange = (ev) => {
        selected = parseInt(window.location.hash.slice(1));
        // posts = JSON.parse(JSON.stringify(posts));
    };

    export let posts = ALL_POSTS.map(({ result }) => result);
</script>

<Header title="CS348 Piazza" />
<div class="content">
    <Sidebar posts={titles} {selected} />
    <Content post={posts.find((el) => el.nr === selected)} {students} />
</div>

<style>
    .content {
        display: flex;
        flex-direction: row;
    }

    :global(a) {
        color: #3c7cc0;
    }
</style>
