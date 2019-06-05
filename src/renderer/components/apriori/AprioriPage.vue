<template>
    <div>
        <el-input
                type="textarea"
                :rows="30"
                placeholder="请输入内容"
                v-model="textarea">
        </el-input>
    </div>
</template>

<script>
    export default {
      name: 'AprioriPage',
      mounted: {

      },
      data () {
        return {
          textarea: 'dsds'
        }
      },
      methods: {
        init: function () {
          // eslint-disable-next-line no-unused-expressions
          self.$http
        }
      }
    }
</script>

<style scoped>

</style>