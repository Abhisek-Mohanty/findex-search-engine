import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ConstantService } from "./constant-service"

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
protected readonly title = signal('findex-search');
public searchQuery: string = '';
public typedText: string = '';
private fullText: string = "Findex.";

constructor(private constantService: ConstantService){
}

ngOnInit(){
  this.typeEffect()
  this.constantService.getCrawl({}).subscribe((res)=>{
    console.log("service file");
    console.log(res);
  })
}


  openSearch(){
    console.log(this.searchQuery);
  }

  async typeEffect() {
    const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
    
    for (let i = 0; i <= this.fullText.length; i++) {
      this.typedText = this.fullText.substring(0, i);
      await sleep(100); 
    }
  }

  getCrawl(){
  this.constantService.getCrawl({}).subscribe((res)=>{
    console.log("service file");
    console.log(res);
  })

  }
}