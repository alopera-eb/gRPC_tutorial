# gRPC Tutorial - Overcooked gRPC!


## Useful Commands
Generate grpc code:
````
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto
````

## Overcooked gRPC
<img src="https://cdn02.nintendo-europe.com/media/images/06_screenshots/games_5/nintendo_switch_download_software_2/nswitchds_overcookedallyoucaneat/NSwitchDS_OvercookedAllYouCanEat_05.jpg">

### Server Calls
- **makeSoup(type)**
    - type: onion, tomato, mushroom
    - return dish, availableDishes --;
- **cleanPlate()**: availableDishes ++;
- **makeBurger(ingredients)**:
    - ingredients: [meat, tomato, lettuce] (Could be a checkbox)
    - return dish, availableDishes --;
- **makeBurrito(ingredients)**:
    - ingredients: [beans, chicken, meat, veggie] (could be a checkbox)
    - return dish, availableDishes --;
- **getCookingStats()**:
    - return cookingStats
- **initGame(availableTime, availableDishes)**:
    - return ok

### Data Formats
```
restaurantStats {
    dishesSold: {}
    earnings: Float
    timeLeft:
}
dish: {
    ingredients: []
    price:[]
}
```
