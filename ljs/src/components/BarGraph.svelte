<script>
    // Let's assume we have the following ages array for this example
    let ages = [5, 12, 24, 37, 45, 58, 65, 72, 89, 100, 101, 110];

    let bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
    let bin_dict = { "0-10": [] };

    // Create bins dynamically
    for (let i = 0; i < bins.length - 1; i++) {
        bin_dict[(bins[i] + 1) + "-" + bins[i + 1]] = [];
    }
    bin_dict["100+"] = [];

    console.log("Empty bin_dict:", bin_dict);

    // Populate the bin_dict with ages
    for (let age of ages) {
        if (age <= 10) {
            bin_dict["0-10"].push(age);
        } else if (age > 100) {
            bin_dict["100+"].push(age);
        } else {
            for (let i = 0; i < bins.length - 1; i++) {
                if (age > bins[i] && age <= bins[i + 1]) {
                    bin_dict[(bins[i] + 1) + "-" + bins[i + 1]].push(age);
                    break;
                }
            }
        }
    }

    console.log("Populated bin_dict:", bin_dict);
</script>

