<template>
    <div>
        <el-table
                :data="this.tableData"
                height="300"
                border
                style="width: 100%" >
            <el-table-column
                    v-for="{ prop, label } in colConfigs"
                    :key="prop"
                    :prop="prop"
                    :label="label">

            </el-table-column>

        </el-table>
        <el-badge></el-badge>
        <div style="text-align:center" slot="header">
            <el-button type="primary" round @click="run" >进行关联规则转化</el-button>

        </div>
        <el-table
                :data="this.resultData"
                height="300"
                border
                style="width: 100%" >
            <el-table-column
                    v-for="{ prop, label } in resultConfig"
                    :key="prop"
                    :prop="prop"
                    :label="label">
            </el-table-column>
        </el-table>
    </div>

</template>

<script>
  export default {
    name: 'AprioriPage',
    mounted: function () {
      this.init()
    },
    data: function () {
      this.colConfigs = [
        {prop: 'index', label: '数据索引'},
        {prop: 'item', label: '一起买的订单编号'}
      ]
      this.resultConfig = [
        {prop: 'item-base', label: '基项集'},
        {prop: 'item-add', label: '目标项集'},
        {prop: 'support', label: '支持度'},
        {prop: 'confidence', label: '关联度'}
      ]
      return {
        tableData: [],
        resultData: []
      }
    },
    methods: {
      init: function () {
        // eslint-disable-next-line no-unused-expressions
        // 初始化数据，得到要进行aprior运算的数据
        this.$http.get('apriori/getdata').then((response) => {
          this.tableData = response.data
          console.info(response.data)
        }).catch(function (error) {
          console.info(error)
        })
      },
      run: function () {
        // 得到进行apriori算法运行后的数据
        this.$http.get('apriori/getresult').then((response) => {
          this.resultData = response.data
          console.info(response.data)
        }).catch(function (error) {
          console.info(error)
        })
      }

    }
  }
</script>

<style scoped>

</style>