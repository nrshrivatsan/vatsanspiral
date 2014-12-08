package main

import (
	"image"
	"image/color"
	"image/draw"
	"image/png"
	"log"
	"os"
	"time"
	"sync"
)

var (
	white  color.Color = color.RGBA{255, 255, 255, 255}
	// black  color.Color = color.RGBA{0, 0, 0, 255}
	// red    color.Color = color.RGBA{125, 0, 0, 255}
	// blue   color.Color = color.RGBA{0, 0, 255, 255}
	cyan   color.Color = color.RGBA{0, 255, 255, 255}
	width  int = 90
	height int = 90
	m *image.RGBA = image.NewRGBA(image.Rect(0, 0, width, height)) //*NRGBA (image.Image interface)
	fileName string = "i.png"
)

// ref) http://golang.org/doc/articles/image_draw.html
func main() {
	
	setPixels(GetArray())
	
}

func GetArray() [][]int {
	array := make([][]int, width)
	for i, _ := range array {
		array[i] = make([]int, width)
		for j, _ := range array {
			if time.Now().Nanosecond()%3 == 0 {
				array[i][j] = 1				
			}
		}
	}
	return array
}

func setPixels( array [][]int ) {
	var wg sync.WaitGroup 

	draw.Draw(m, m.Bounds(), &image.Uniform{white}, image.ZP, draw.Src)
	

	for i, _ := range array {
		for j, _ := range array {
			if array[i][j] == 1 {
				wg.Add(1)
				go func( i int, j int ) {
					 m.Set(j, i, white)
					 defer wg.Done()
				}(i,j)
			
			} else {
				wg.Add(1)

			go func( i int, j int ) {
					 m.Set(j, i, cyan)
					 defer wg.Done()
				}(i,j)
			}
		}
	}

	wg.Wait()
	WriteToFile()
}

func WriteToFile() {
	
	w, err := os.Create(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer w.Close()

	// jpeg.Encode(file, m, &jpeg.Options{80})
	png.Encode(w, m) //Encode writes the Image m to w in PNG format.

}