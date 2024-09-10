<script>

    //export let ages

    let bins = [10,20,30,40,50,60,70,80,90,100]

    let bin_dict = {"0-10" : []}

    console.log(bin_dict)

    for (let i = 0; i < (bins.length -1 ); i ++) {
        bin_dict[(bins[i] + 1) + "-" + bins[i+1]] = []
    }

    bin_dict["100+"] = []

    console.log(bin_dict)

    //for (let i = 0; i < ages.length; i ++) {

   // }


</script>