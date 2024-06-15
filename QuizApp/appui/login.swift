struct ContentView : View {
    var body: some View {
        VStack {
            
        }
    }
}
struct ContentView : View {
    var body: some View {
        VStack {
            Text("Welcome!")
                .font(.largeTitle)
                .fontWeight(.semibold)
                .padding(.bottom, 20)
        }
    }
}
struct ContentView : View {
    var body: some View {
        VStack {
            WelcomeText()
            Image("userImage")
        }
    }
}
struct ContentView : View {
    var body: some View {
        VStack {
            WelcomeText()
            Image("userImage")
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(width: 150, height: 150)
                .clipped()
                .cornerRadius(150)
                .padding(.bottom, 75)
        }
    }
}