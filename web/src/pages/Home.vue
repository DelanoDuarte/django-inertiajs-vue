<template>
    <div>
        <div>
            <h1>Home</h1>
        </div>

        <div>
            <h2>Msg from Django Server</h2>
            <p>{{ text }}</p>
        </div>

        <div>
            <HelloWorld msg="Hello Vue 3 + Vite" />
        </div>
    </div>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue'
export default {
    components: {
        HelloWorld
    },
    props: {
        text: String
    },
}
</script>

<style></style>