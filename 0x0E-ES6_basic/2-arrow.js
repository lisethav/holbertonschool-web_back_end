export default function getNeighborhoodsList() {
    this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

    const selft = this;
    this.addNeighborhood = (newNeighborhood) => {
        selft.sanFranciscoNeighborhoods.push(newNeighborhood);
        return selft.sanFranciscoNeighborhoods;
    };
}
