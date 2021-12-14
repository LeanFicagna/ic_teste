<template>
    <div>
        <h1 class="diferente">{{ mensagem }}</h1>
    </div>
</template>

<script>
export default {
    name: 'Teste',
    data() {
        return {
            mensagem: 'Minha mensagem via meu component'
        }
    }
}
</script>

<style>
    h1.diferente {
        background: #333;
        color: #fff;
    }
</style>