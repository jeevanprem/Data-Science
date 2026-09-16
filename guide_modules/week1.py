# -*- coding: utf-8 -*-
"""Week 1 Module: Introduction to R & Programming Foundations"""

def get_week1_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 1 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week1">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 01</span> Introduction to R &amp; Programming Foundations</h2>
                    <div class="module-lectures">NPTEL Lectures 01–11 | Course Philosophy, Workspace, Data Structures, Control Flow, and Functions</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        R is a high-level interpreted programming language and environment specifically optimized for statistical computing, linear algebra, and data science. Unlike general-purpose languages, R treats vectors as primitive entities, executing calculations natively via SIMD (Single Instruction, Multiple Data) vectorization.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Workspace &amp; Environment Architecture</h4>
                        <p>
                            The R interactive session maintains an active workspace in system RAM. Variables, vectors, models, and custom functions exist within the global environment.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><code class="inline-code">ls()</code>: Lists names of all active variables and objects residing in the working memory. <em>(Exam trap: it does NOT list filesystem directory contents!)</em></li>
                            <li><code class="inline-code">rm(list = ls())</code>: Clears the entire workspace memory.</li>
                            <li><code class="inline-code">getwd()</code> / <code class="inline-code">setwd(dir)</code>: Queries or sets the operating system working directory for relative file I/O.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Atomic Data Types &amp; Coercion Hierarchy</h4>
                        <p>
                            R features six primary atomic types: <strong>logical</strong>, <strong>integer</strong> (e.g., <code class="inline-code">10L</code>), <strong>numeric</strong> (double precision float, e.g., <code class="inline-code">10.5</code>), <strong>complex</strong> (e.g., <code class="inline-code">2 + 3i</code>), <strong>character</strong> (strings), and <strong>raw</strong> (bytes). When combining mixed types within an atomic vector, R applies automatic coercive promotion:
                        </p>
                        <div style="text-align: center; margin: 10px 0; font-weight: 600; color: var(--primary-navy);">
                            Logical $\longrightarrow$ Integer $\longrightarrow$ Numeric (Double) $\longrightarrow$ Character
                        </div>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Core Data Structures</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Vectors:</strong> 1-dimensional, strictly homogeneous. Created via <code class="inline-code">c(...)</code> or sequence generators <code class="inline-code">1:n</code>, <code class="inline-code">seq()</code>.</li>
                            <li><strong>Matrices:</strong> 2-dimensional, strictly homogeneous. Created using <code class="inline-code">matrix(data, nrow, ncol, byrow = FALSE)</code>. By default, R populates matrices column-by-column (<code class="inline-code">byrow = FALSE</code>).</li>
                            <li><strong>Lists:</strong> 1-dimensional, <em>heterogeneous</em> recursive containers. Can hold vectors, matrices, nested lists, and data frames simultaneously.
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li><code class="inline-code">list[k]</code>: Returns a <strong>sub-list</strong> containing the $k$-th element (retains list container).</li>
                                    <li><code class="inline-code">list[[k]]</code>: Extracts the <strong>naked content</strong> of the $k$-th element.</li>
                                    <li><code class="inline-code">list[[4]][2]</code>: Extracts the 4th element's 2nd internal component.</li>
                                </ul>
                            </li>
                            <li><strong>Data Frames:</strong> 2-dimensional, heterogeneous tabular structures where each column is a vector of identical length. Access columns via <code class="inline-code">df$column_name</code> or <code class="inline-code">df[["column_name"]]</code>.</li>
                            <li><strong>Factors:</strong> Categorical variables storing integer codes mapped to string <code class="inline-code">levels</code>.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Operators &amp; Control Flow Rules</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Logical Operators:</strong> <code class="inline-code">&amp;</code> and <code class="inline-code">|</code> perform vectorized element-by-element boolean logic. <code class="inline-code">&amp;&amp;</code> and <code class="inline-code">||</code> evaluate only the first element (short-circuit scalar evaluation for <code class="inline-code">if</code> statements).</li>
                            <li><strong>Membership Operator:</strong> <code class="inline-code">%in%</code> checks if elements of the left vector exist anywhere in the right vector, returning a boolean vector.</li>
                            <li><strong>Matrix Product:</strong> <code class="inline-code">%*%</code> computes inner linear algebra matrix multiplication, requiring matching inner dimensions ($m \\times k$ with $k \\times n$). Standard <code class="inline-code">*</code> computes element-wise Hadamard product!</li>
                            <li><strong>Loop Constructs:</strong>
                                <br>• <code class="inline-code">for (var in seq) { ... }</code>: Iterates sequentially through each element in a vector.
                                <br>• <code class="inline-code">while (condition) { ... }</code>: Repeats code block while condition remains <code class="inline-code">TRUE</code>.
                                <br>• <code class="inline-code">repeat { ... if (cond) break }</code>: Executes indefinitely until explicitly terminated via <code class="inline-code">break</code>.
                                <br>• <code class="inline-code">next</code>: Skips remainder of current loop iteration and advances counter.
                                <br>• <code class="inline-code">break</code>: Terminates the loop structure immediately.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. String Concatenation &amp; User Input</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>paste() vs paste0():</strong>
                                <br>• <code class="inline-code">paste(..., sep = " ", collapse = NULL)</code>: Joins elements with a default space separator.
                                <br>• <code class="inline-code">paste0(...)</code>: Fast shortcut for <code class="inline-code">paste(..., sep = "")</code> with zero separation.
                                <br>• <strong>sep vs collapse (Exam Core):</strong> <code class="inline-code">sep</code> is placed between separate argument terms for each corresponding index. <code class="inline-code">collapse</code> collapses the resulting character vector into a single scalar string delimited by the specified token.
                            </li>
                            <li><strong>Console Input &amp; Coercion:</strong> <code class="inline-code">readline(prompt = "...")</code> captures input as character data. Numeric computation requires explicit conversion via <code class="inline-code">as.integer()</code> or <code class="inline-code">as.numeric()</code>.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">F. Reshaping &amp; Merging Data (Lec 6)</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>reshape2 Package:</strong>
                                <br>• <code class="inline-code">melt(data, id.vars, measure.vars)</code>: Wide-to-long transformation.
                                <br>• <code class="inline-code">dcast(data, formula, fun.aggregate)</code>: Long-to-wide pivot aggregation.
                            </li>
                            <li><strong>merge(x, y, by = ...):</strong>
                                <br>• Inner Join (<code class="inline-code">all = FALSE</code>): Keeps only matching keys present in both frames.
                                <br>• Left Join (<code class="inline-code">all.x = TRUE</code>): Retains all rows from <code class="inline-code">x</code>, filling unmatched <code class="inline-code">y</code> with <code class="inline-code">NA</code>.
                                <br>• Full Outer Join (<code class="inline-code">all = TRUE</code>): Retains all rows from both tables.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">G. Exploratory Data Inspection &amp; Missing Values</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><code class="inline-code">str(df)</code>: Displays compact structural overview (dimensions, column types, first few observations).</li>
                            <li><code class="inline-code">summary(df)</code>: Computes five-number summary (Min, $Q_1$, Median, Mean, $Q_3$, Max) for numeric features, frequency tables for factors.</li>
                            <li><code class="inline-code">dim(df)</code>, <code class="inline-code">nrow(df)</code>, <code class="inline-code">ncol(df)</code>: Return row and column dimensions.</li>
                            <li><strong>Missing Data (<code class="inline-code">NA</code>):</strong> <code class="inline-code">is.na(x)</code> detects missing values; <code class="inline-code">sum(is.na(df))</code> counts missing values; <code class="inline-code">na.omit(df)</code> removes incomplete rows.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">H. Base Graphics &amp; Visualization (Lec 11)</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><code class="inline-code">plot(x, y, type = "p", main, xlab, ylab)</code>: Creates scatter plots (<code class="inline-code">"p"</code>), line plots (<code class="inline-code">"l"</code>), or both (<code class="inline-code">"b"</code>).</li>
                            <li><code class="inline-code">hist(x, breaks, freq = TRUE)</code>: Visualizes continuous frequency distribution (<code class="inline-code">freq = FALSE</code> yields probability density).</li>
                            <li><code class="inline-code">boxplot(x)</code>: Plots median, quartiles, and statistical outliers beyond $1.5 \\times \\text{IQR}$.</li>
                            <li><code class="inline-code">barplot(height)</code>: Displays bar chart of categorical frequencies.</li>
                            <li><code class="inline-code">lines()</code>, <code class="inline-code">points()</code>, <code class="inline-code">legend()</code>: Add supplementary layers to an active graphic window.</li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Negative Indexing in R vs Python</h4>
                            <p>
                                In Python, a negative index like <code class="inline-code">a[-1]</code> accesses the last element. In R, negative indices mean <strong>exclusion / dropping</strong>! For instance, <code class="inline-code">A[-2, ]</code> removes the 2nd row and returns a matrix with all remaining rows. Similarly, <code class="inline-code">v[-3]</code> drops the 3rd element.
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's Blueprint: Deconstructing R Nested Subsetting</h4>
                            <p>
                                When evaluating complex nested structures like <code class="inline-code">data$col[condition] &lt;- value</code> or <code class="inline-code">nested_list[[i]][j]</code>:
                                <br>1. Evaluate innermost bracket first: resolve the index or logical mask.
                                <br>2. Check container types: Single brackets <code class="inline-code">[ ]</code> preserve the parent class; double brackets <code class="inline-code">[[ ]]</code> extract the underlying element.
                                <br>3. Pay close attention to logical vector alignment: R recycles short vectors if their length evenly divides the target vector.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Mathematical Rules &amp; Vectorization Principles</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Vector Recycling Rule</span>
                                <span class="nav-badge">Rule</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{length}(v_1) \\pmod{\\text{length}(v_2)} = 0$$
                            </div>
                            <div class="formula-desc">When operating on two vectors of unequal length, R automatically repeats the shorter vector until it matches the longer vector's length. A warning occurs if not an exact multiple.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If <code>x &lt;- c(1, 2, 3, 4)</code> and <code>y &lt;- c(10, 20)</code>, what is <code>x + y</code>?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Length 4 is an exact multiple of 2 ($4 \\pmod 2 = 0$). Vector <code>y</code> recycles to <code>c(10, 20, 10, 20)</code>. Result: <code>c(11, 22, 13, 24)</code> (no warning).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is the output and warning for <code>c(1, 2, 3) + c(1, 2)</code>?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Length 3 is not a multiple of 2. Shorter vector recycles partially to <code>c(1, 2, 1)</code> producing <code>c(2, 4, 4)</code> with warning: <em>"longer object length is not a multiple of shorter object length"</em>.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Matrix Multiplication Dimension Match</span>
                                <span class="nav-badge">Linear Algebra</span>
                            </div>
                            <div class="formula-math">
                                $$A_{(m \\times k)} \\mathbin{\\%*\\%} B_{(k \\times n)} = C_{(m \\times n)}$$
                            </div>
                            <div class="formula-desc">Inner dimensions must match ($k = k$). Element $(i,j)$ is the dot product of row $i$ of $A$ and column $j$ of $B$: $C_{ij} = \\sum_{r=1}^k A_{ir} B_{rj}$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If matrix $A$ is $3 \\times 4$ and matrix $B$ is $4 \\times 2$, what is the dimension of $A \\mathbin{\\%*\\%} B$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Inner dimensions match ($4 = 4$). The resulting product $C$ has dimension $3 \\times 2$. Attempting $B \\mathbin{\\%*\\%} A$ throws an error ($2 \\ne 3$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For column vectors $u = [1, 2, 3]^T$ and $v = [4, 5, 6]^T$ ($3 \\times 1$), how to get the scalar dot product in R?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Compute <code>t(u) %*% v</code> which is $(1 \\times 3) \\times (3 \\times 1) = [32]$. In contrast, <code>u * v</code> gives element-wise product <code>c(4, 10, 18)</code>.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Negative Subsetting Rule</span>
                                <span class="nav-badge">R Syntax</span>
                            </div>
                            <div class="formula-math">
                                $$A_{[-r, \\:]} = \\{A_{i, \\:} \\mid i \\in \\{1,\\dots,m\\} \\setminus \\{r\\}\\}$$
                            </div>
                            <div class="formula-desc">Negative row or column index deletes that row/column from the returned matrix or data frame.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given a $4 \\times 4$ matrix $M$, what does <code>M[-2, -c(1, 3)]</code> return?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Deletes row 2 and columns 1 &amp; 3. The returned submatrix has dimension $3 \\times 2$ (rows 1, 3, 4 and columns 2, 4).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For vector <code>v &lt;- c(10, 20, 30, 40, 50)</code>, what is <code>v[-c(1, 4)]</code>?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Omits elements at index 1 (10) and index 4 (40). Result: <code>c(20, 30, 50)</code>. (Note: R does not allow mixing positive and negative indices).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>String Concatenation (sep vs collapse)</span>
                                <span class="nav-badge">R Syntax</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{paste}(v_1, v_2, \\text{sep}=\\sigma), \\quad \\text{paste}(v, \\text{collapse}=\\kappa)$$
                            </div>
                            <div class="formula-desc"><code class="inline-code">sep</code> joins corresponding elements across vector arguments; <code class="inline-code">collapse</code> squashes all elements into a single scalar string.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> What is <code>paste(c("A","B"), c(1,2), sep="-")</code> vs <code>paste(c("A","B"), collapse="-")</code>?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> With <code>sep = "-"</code>, elements are joined pairwise yielding vector <code>c("A-1", "B-2")</code>. With <code>collapse = "-"</code>, vector elements are collapsed into scalar <code>"A-B"</code>.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What does <code>paste0("Var_", 1:3)</code> return?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> <code>paste0()</code> defaults to zero separator (<code>sep=""</code>). R recycles <code>"Var_"</code> across <code>1:3</code> returning <code>c("Var_1", "Var_2", "Var_3")</code>.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Boxplot Whiskers &amp; Outlier Rule</span>
                                <span class="nav-badge">Graphics &amp; EDA</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{IQR} = Q_3 - Q_1, \\quad [Q_1 - 1.5 \\times \\text{IQR}, \\; Q_3 + 1.5 \\times \\text{IQR}]$$
                            </div>
                            <div class="formula-desc">Whiskers extend to the most extreme data points within $1.5 \\times \\text{IQR}$. Data points falling beyond the fences are plotted individually as outliers.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If $Q_1 = 20$ and $Q_3 = 35$, compute the upper threshold for outlier detection.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{IQR} = 35 - 20 = 15$. Upper fence: $Q_3 + 1.5(\\text{IQR}) = 35 + 1.5(15) = 57.5$. Any value $> 57.5$ is flagged as an outlier.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For the same dataset, is an observation of $-5$ an outlier?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Lower fence: $Q_1 - 1.5(\\text{IQR}) = 20 - 22.5 = -2.5$. Since $-5 &lt; -2.5$, the observation is an outlier.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>


                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Functions Reference Table</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Syntax</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Description &amp; Operation</th>
                                    <th>Practical Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">ls()</span></td>
                                    <td><code class="inline-code">ls(name, envir)</code></td>
                                    <td>Returns character vector of object names in the current environment.</td>
                                    <td><code class="inline-code">x &lt;- 5; ls()</code></td>
                                    <td><code class="inline-code">"x"</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">c(...)</span></td>
                                    <td><code class="inline-code">c(..., recursive=F)</code></td>
                                    <td>Combines values into an atomic vector. Automatically coerces types.</td>
                                    <td><code class="inline-code">c(1, TRUE, "A")</code></td>
                                    <td><code class="inline-code">c("1", "TRUE", "A")</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">matrix()</span></td>
                                    <td><code class="inline-code">matrix(data, nrow, ncol, byrow)</code></td>
                                    <td>Constructs a 2D matrix. Populates column-wise unless <code class="inline-code">byrow=TRUE</code>.</td>
                                    <td><code class="inline-code">matrix(1:6, nrow=2, byrow=T)</code></td>
                                    <td>$2 \\times 3$ matrix with row 1 as [1,2,3]</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">list()</span></td>
                                    <td><code class="inline-code">list(...)</code></td>
                                    <td>Constructs a generic vector containing elements of any types.</td>
                                    <td><code class="inline-code">list(a=1:3, b="NPTEL")</code></td>
                                    <td>Named heterogeneous list</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">data.frame()</span></td>
                                    <td><code class="inline-code">data.frame(...)</code></td>
                                    <td>Tightly coupled collection of variables with equal row count.</td>
                                    <td><code class="inline-code">data.frame(id=1:2, g=c("M","F"))</code></td>
                                    <td>$2 \\times 2$ tabular data frame</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">paste()</span></td>
                                    <td><code class="inline-code">paste(..., sep=" ", collapse=NULL)</code></td>
                                    <td>Concatenates strings. <code class="inline-code">sep</code> joins parallel elements; <code class="inline-code">collapse</code> collapses vector into single string.</td>
                                    <td><code class="inline-code">paste(c("A","B"), collapse="-")</code></td>
                                    <td><code class="inline-code">"A-B"</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">%in%</span></td>
                                    <td><code class="inline-code">x %in% table</code></td>
                                    <td>Value matching: returns logical vector indicating whether each element in <code class="inline-code">x</code> matches in <code class="inline-code">table</code>.</td>
                                    <td><code class="inline-code">c(2, 5) %in% 1:3</code></td>
                                    <td><code class="inline-code">c(TRUE, FALSE)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">which()</span></td>
                                    <td><code class="inline-code">which(x, arr.ind=F)</code></td>
                                    <td>Returns integer indices where boolean condition <code class="inline-code">x</code> is <code class="inline-code">TRUE</code>.</td>
                                    <td><code class="inline-code">which(c(10, 20, 30) &gt; 15)</code></td>
                                    <td><code class="inline-code">c(2, 3)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">rbind() / cbind()</span></td>
                                    <td><code class="inline-code">rbind(...), cbind(...)</code></td>
                                    <td>Binds matrices/vectors row-wise or column-wise.</td>
                                    <td><code class="inline-code">cbind(c(1,2), c(3,4))</code></td>
                                    <td>$2 \\times 2$ matrix with columns [1,2] &amp; [3,4]</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">apply()</span></td>
                                    <td><code class="inline-code">apply(X, MARGIN, FUN)</code></td>
                                    <td>Applies function over array margins (1 = rows, 2 = columns).</td>
                                    <td><code class="inline-code">apply(M, 2, mean)</code></td>
                                    <td>Vector of column means</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">paste0(...)</span></td>
                                    <td><code class="inline-code">paste0(...)</code></td>
                                    <td>Shortcut for <code class="inline-code">paste(..., sep="")</code> with zero-width separator.</td>
                                    <td><code class="inline-code">paste0("X", 1:3)</code></td>
                                    <td><code class="inline-code">c("X1", "X2", "X3")</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">readline()</span></td>
                                    <td><code class="inline-code">readline(prompt="")</code></td>
                                    <td>Reads a single line of user input from the console as a character string.</td>
                                    <td><code class="inline-code">val &lt;- as.numeric(readline("Enter N: "))</code></td>
                                    <td>Prompts user, returns parsed numeric value</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">melt()</span></td>
                                    <td><code class="inline-code">melt(data, id.vars, measure.vars)</code></td>
                                    <td>Reshapes wide data frame into tall/long format (from package <code class="inline-code">reshape2</code>).</td>
                                    <td><code class="inline-code">melt(df, id.vars="id")</code></td>
                                    <td>Tall data frame with variable and value columns</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">dcast()</span></td>
                                    <td><code class="inline-code">dcast(data, formula, fun.aggregate)</code></td>
                                    <td>Casts molten long data into wide cross-tabulated format.</td>
                                    <td><code class="inline-code">dcast(m, id ~ variable)</code></td>
                                    <td>Wide rectangular data frame</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">merge()</span></td>
                                    <td><code class="inline-code">merge(x, y, by, all, all.x, all.y)</code></td>
                                    <td>Joins two data frames by common key columns (inner, left, right, full outer joins).</td>
                                    <td><code class="inline-code">merge(df1, df2, by="ID", all.x=TRUE)</code></td>
                                    <td>Merged data frame with left outer join</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">boxplot()</span></td>
                                    <td><code class="inline-code">boxplot(x, horizontal=FALSE)</code></td>
                                    <td>Plots five-number summary: min, $Q_1$, median, $Q_3$, max and outliers.</td>
                                    <td><code class="inline-code">boxplot(salary ~ dept, data=df)</code></td>
                                    <td>Comparative box-and-whisker plot</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">hist() / barplot()</span></td>
                                    <td><code class="inline-code">hist(x, breaks), barplot(height)</code></td>
                                    <td><code class="inline-code">hist()</code> shows frequency of continuous data; <code class="inline-code">barplot()</code> plots counts of categorical factors.</td>
                                    <td><code class="inline-code">hist(x, breaks=10); barplot(table(cat))</code></td>
                                    <td>Continuous frequency histogram / discrete bar chart</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">str() / summary()</span></td>
                                    <td><code class="inline-code">str(object), summary(object)</code></td>
                                    <td><code class="inline-code">str()</code> inspects internal structure/data types; <code class="inline-code">summary()</code> gives statistical summaries.</td>
                                    <td><code class="inline-code">str(df); summary(df$age)</code></td>
                                    <td>Schema structure and 5-number summary + mean</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">is.na() / na.omit()</span></td>
                                    <td><code class="inline-code">is.na(x), na.omit(object)</code></td>
                                    <td>Tests for missing values (<code class="inline-code">NA</code>) or strips rows containing missing values.</td>
                                    <td><code class="inline-code">sum(is.na(df)); clean &lt;- na.omit(df)</code></td>
                                    <td>Count of missing values / cleaned data frame</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Nested List Subsetting</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Consider the list definition given below:</p>
                            <pre class="r-code">city_weather &lt;- list(
  "City A",
  "City B",
  "City C",
  c("Sunny", "cloudy", "Rainy")
)</pre>
                            <p>Which of the following commands correctly accesses the string <code class="inline-code">"cloudy"</code>?</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> <code class="inline-code">city_weather[[4]][2]</code></li>
                                <li><span class="opt-bullet">B.</span> <code class="inline-code">city_weather[[5]]</code></li>
                                <li><span class="opt-bullet">C.</span> <code class="inline-code">city_weather[[2]][2]</code></li>
                                <li><span class="opt-bullet">D.</span> <code class="inline-code">city_weather[4][2]</code></li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Analyze the Container Architecture</div>
                                    <p>The list <code class="inline-code">city_weather</code> contains 4 top-level elements: index 1 is <code class="inline-code">"City A"</code>, index 2 is <code class="inline-code">"City B"</code>, index 3 is <code class="inline-code">"City C"</code>, and index 4 is a character vector <code class="inline-code">c("Sunny", "cloudy", "Rainy")</code>.</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Apply Double-Bracket Extraction</div>
                                    <p><code class="inline-code">city_weather[[4]]</code> unwraps the list container and yields the raw vector <code class="inline-code">c("Sunny", "cloudy", "Rainy")</code>.</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Index into the Vector</div>
                                    <p>The target element <code class="inline-code">"cloudy"</code> is at position 2 of this character vector. Hence, indexing with <code class="inline-code">[2]</code> gives <code class="inline-code">city_weather[[4]][2]</code>.</p>
                                    <p><em>Exam Note:</em> Single bracket <code class="inline-code">city_weather[4]</code> returns a list of length 1, so <code class="inline-code">city_weather[4][2]</code> yields <code class="inline-code">NULL</code>!</p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (<code class="inline-code">city_weather[[4]][2]</code>)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Matrix Negative Row Indexing</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> Consider the following R code snippet:</p>
                            <pre class="r-code">A &lt;- matrix(c(1:42), nrow = 6, ncol = 7, byrow = TRUE)
B &lt;- A[-2, ]</pre>
                            <p>What does matrix <code class="inline-code">B</code> represent?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> A matrix consisting only of the elements in the 2nd row of <code class="inline-code">A</code>.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> A matrix containing all elements of <code class="inline-code">A</code> except for the 2nd row.</li>
                                <li><span class="opt-bullet">C.</span> A matrix containing the elements of the 2nd row from the bottom of <code class="inline-code">A</code>.</li>
                                <li><span class="opt-bullet">D.</span> An error occurs due to invalid negative subscripting.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Understand Matrix Dimensions</div>
                                    <p>Matrix <code class="inline-code">A</code> has 6 rows and 7 columns ($6 \\times 7 = 42$ entries), populated row-by-row because <code class="inline-code">byrow = TRUE</code>.</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Understand Negative Slicing in R</div>
                                    <p>In R syntax, the index format is <code class="inline-code">[row, column]</code>. The minus prefix <code class="inline-code">-k</code> indicates the deletion/omission of index $k$. Therefore, <code class="inline-code">A[-2, ]</code> means "omit row 2 and retain all columns". The resulting matrix <code class="inline-code">B</code> has dimension $5 \\times 7$.</p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B (A matrix containing all elements of A except for the 2nd row)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: String Manipulation with paste()</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> What is the distinct role of the parameter <code class="inline-code">collapse</code> in the function <code class="inline-code">paste()</code>?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> It specifies the separator used to join parallel elements across multiple vectors.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> It separates the values of the resulting character vector into a single consolidated string.</li>
                                <li><span class="opt-bullet">C.</span> It deletes whitespace from all character elements.</li>
                                <li><span class="opt-bullet">D.</span> It folds multi-dimensional arrays into flat vectors.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Compare sep vs collapse</div>
                                    <p>In R, <code class="inline-code">paste()</code> takes two delimiter arguments:</p>
                                    <ul style="margin-left: 18px;">
                                        <li><code class="inline-code">sep = "..."</code>: Defines the delimiter used when concatenating corresponding elements from multiple vectors term-by-term. Returns a vector of length equal to max vector length.</li>
                                        <li><code class="inline-code">collapse = "..."</code>: Collapses all elements of the final character vector into a single atomic string separated by the string provided.</li>
                                    </ul>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Demonstration</div>
                                    <pre class="r-code">paste(c("X", "Y"), c("1", "2"), sep = "_")
# Output: [1] "X_1" "Y_2" (length 2)

paste(c("X", "Y"), c("1", "2"), sep = "_", collapse = " &amp; ")
# Output: [1] "X_1 &amp; Y_2" (length 1)</pre>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B (Separates the values of the resulting character vector into a single consolidated string)
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 1 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: Data Frame Conditional Mutation &amp; Loop Execution Tracing
                            </p>
                            <p>
                                An environmental sensor records temperature in three metropolitan regions. A research engineer writes the following R program to update erroneous records and perform automated status logging:
                            </p>
                            <pre class="r-code"># Part A: Data Frame Manipulation
name &lt;- c("City A", "City B", "City C")
weather &lt;- c("Sunny", "cloudy", "Rainy")
city_data &lt;- data.frame(name, weather, stringsAsFactors = FALSE)

# Conditional Replacement
city_data$weather[city_data$name == "City C"] &lt;- "Snowy"

# Part B: Algorithmic Loop with 'next' Flow Control
temp_readings &lt;- c(15, 20, 28, 12, 22)
logged_status &lt;- character()

for (temp in temp_readings) {
  if (temp &lt; 18) {
    next # Skip cold days
  }
  if (temp &gt;= 18 &amp;&amp; temp &lt;= 25) {
    logged_status &lt;- c(logged_status, "Optimal")
  } else {
    logged_status &lt;- c(logged_status, "High")
  }
}</pre>

                            <p style="margin-top: 12px; font-weight: 600;">Answer the following questions:</p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem;">
                                <li>What is the exact content of the <code class="inline-code">weather</code> column in <code class="inline-code">city_data</code> after the conditional replacement?</li>
                                <li>What is the length and final contents of the <code class="inline-code">logged_status</code> character vector?</li>
                                <li>What would happen if the assignment used single brackets <code class="inline-code">&amp;</code> instead of <code class="inline-code">&amp;&amp;</code> inside the <code class="inline-code">if</code> conditional?</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Solution to Part 1: Data Frame Conditional Modification</div>
                                        <p>
                                            The logical condition <code class="inline-code">city_data$name == "City C"</code> generates the logical boolean vector:
                                            $$\\begin{bmatrix} \\text{"City A" == "City C"} \\\\ \\text{"City B" == "City C"} \\\\ \\text{"City C" == "City C"} \\end{bmatrix} = \\begin{bmatrix} \\text{FALSE} \\\\ \\text{FALSE} \\\\ \\text{TRUE} \\end{bmatrix}$$
                                            Subsetting <code class="inline-code">city_data$weather[...]</code> selects only the 3rd element, which was initially <code class="inline-code">"Rainy"</code>.
                                            The assignment <code class="inline-code">&lt;- "Snowy"</code> overwrites row 3. The resulting column is:
                                            <br><strong>Row 1:</strong> <code class="inline-code">Sunny</code>, <strong>Row 2:</strong> <code class="inline-code">cloudy</code>, <strong>Row 3:</strong> <code class="inline-code">Snowy</code>.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Solution to Part 2: Loop Execution &amp; 'next' Statement Tracing</div>
                                        <p>Tracing through the vector <code class="inline-code">temp_readings &lt;- c(15, 20, 28, 12, 22)</code> step by step:</p>
                                        <table class="academic-table" style="margin: 10px 0; font-size: 0.85rem;">
                                            <thead>
                                                <tr>
                                                    <th>Iteration</th>
                                                    <th>temp Value</th>
                                                    <th>Condition 1: temp &lt; 18</th>
                                                    <th>Action Taken</th>
                                                    <th>logged_status State</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>1</td>
                                                    <td>15</td>
                                                    <td>TRUE (15 &lt; 18)</td>
                                                    <td><code class="inline-code">next</code> executed: skips iteration</td>
                                                    <td><code class="inline-code">character(0)</code></td>
                                                </tr>
                                                <tr>
                                                    <td>2</td>
                                                    <td>20</td>
                                                    <td>FALSE (20 &ge; 18)</td>
                                                    <td>Matches $18 \le 20 \le 25 \implies$ appends "Optimal"</td>
                                                    <td><code class="inline-code">c("Optimal")</code></td>
                                                </tr>
                                                <tr>
                                                    <td>3</td>
                                                    <td>28</td>
                                                    <td>FALSE (28 &ge; 18)</td>
                                                    <td>Fails $\le 25 \implies$ appends "High"</td>
                                                    <td><code class="inline-code">c("Optimal", "High")</code></td>
                                                </tr>
                                                <tr>
                                                    <td>4</td>
                                                    <td>12</td>
                                                    <td>TRUE (12 &lt; 18)</td>
                                                    <td><code class="inline-code">next</code> executed: skips iteration</td>
                                                    <td><code class="inline-code">c("Optimal", "High")</code></td>
                                                </tr>
                                                <tr>
                                                    <td>5</td>
                                                    <td>22</td>
                                                    <td>FALSE (22 &ge; 18)</td>
                                                    <td>Matches $18 \le 22 \le 25 \implies$ appends "Optimal"</td>
                                                    <td><code class="inline-code">c("Optimal", "High", "Optimal")</code></td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        <p>The final vector has length <strong>3</strong> and elements: <code class="inline-code">c("Optimal", "High", "Optimal")</code>.</p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Solution to Part 3: Difference Between &amp; and &amp;&amp; in Control Flow</div>
                                        <p>
                                            In R, the <code class="inline-code">if</code> statement expects a scalar boolean (length 1). When using <code class="inline-code">&amp;&amp;</code>, R performs strict scalar short-circuit evaluation. If single <code class="inline-code">&amp;</code> were used on vector arguments, it would return a logical vector, triggering the warning: <em>"the condition has length &gt; 1 and only the first element will be used"</em>. Here <code class="inline-code">temp</code> is scalar, so both yield the same boolean value, but using <code class="inline-code">&amp;&amp;</code> is best practice and required standard in R control statements.
                                        </p>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Summary: Column 2 becomes [Sunny, cloudy, Snowy]; Logged vector is of length 3: ["Optimal", "High", "Optimal"].
                                    </div>
                                </div>
                            </details>
                        </div>
                    </div>
                </section>
            </div>
        </article>
        <div class="page-break"></div>
"""

print("Week 1 module loaded.")
