module tt_um_Rescobar226_fsm (
    input  wire clk,
    input  wire rst_n,
    input  wire ena,
    input  wire [7:0] ui,
    output wire [7:0] uo,
    inout  wire [7:0] uio
);

    wire Sen = ui[0];
    wire SE  = ui[1];
    wire LA  = ui[2];
    wire LC  = ui[3];

    reg [3:0] S = 4'b0000;
    reg [3:0] S_n;

    always @(*) begin
        S_n[3] = ~S[3] & S[2] & ~S[1] & ~S[0] & ~Sen & ~SE & LA;
        S_n[2] = ~S[3] & ~S[2] & S[1] & ~S[0] & Sen & ~SE & ~LC;
        S_n[1] = (S[3] & ~S[2] & ~S[1] & ~S[0] & ~Sen & SE & ~LA & ~LC) |
                 (~S[3] & ~S[2] & ~S[1] & S[0] & Sen & ~SE & ~LA);
        S_n[0] = (S[3] & ~S[2] & ~S[1] & ~S[0] & ~Sen & ~SE & ~LA & LC) |
                 (~S[3] & ~S[2] & ~S[1] & ~S[0] & Sen & ~SE & ~LA & LC);
    end

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            S <= 4'b0000;
        else if (ena)
            S <= S_n;
    end

    wire MA = (S == 4'b0010);
    wire MC = (S == 4'b0100);

    assign uo[0] = MA;
    assign uo[1] = MC;
    assign uo[2] = S[0];
    assign uo[3] = S[1];
    assign uo[4] = S[2];
    assign uo[5] = S[3];
    assign uo[6] = 1'b0;
    assign uo[7] = 1'b0;

    assign uio = 8'bZ;

endmodule
