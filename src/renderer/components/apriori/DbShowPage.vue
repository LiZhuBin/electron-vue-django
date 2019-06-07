<template>
    <el-tabs type="border-card">
        <el-tab-pane label="时间维数据">
            <
        </el-tab-pane>
        <el-tab-pane label="配置管理">配置管理</el-tab-pane>
        <el-tab-pane label="角色管理">角色管理</el-tab-pane>
        <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
    </el-tabs>
</template>

<script>
  export default {
    name: "DbShowPage",
    data(){
      return{

      }
    },
    methods:{
      initData:function () {
        this.$http.get('')
          .then()
      }
    },
    components:{

    }
  }
</script>

<style scoped>

</style>