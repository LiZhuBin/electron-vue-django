<template>
    <div>
   <Location ></Location>
        <DateSelect></DateSelect>
        <Commodity></Commodity>
        <el-divider></el-divider>

        <Result></Result>
    </div>
</template>

<script>
    import Location from './LocationPage'
    import DateSelect from './DateSelect'
    import Commodity from './CommodityPage'
    import Result from './ResultPage'
  export default {
    name: "AnalysePage",
    data(){
      return{
        selectData: {
          provinces: []
        }
      }
    },
    components:{
      Location,
      DateSelect,
      Commodity,
      Result
    },


  }
</script>

<style scoped>

</style>